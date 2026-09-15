#!/usr/bin/env python3
# IMPLEMENTATION_TEST_ONLY - NOT EXPERIMENTAL EVIDENCE
"""Behavioral tests for SEM-REV-E0 v1 implementation (I1-I10)."""

import ast
import hashlib
import json
import os
import sqlite3
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

IMPL_ROOT = Path(__file__).resolve().parents[1]
SUT_DIR = IMPL_ROOT / 'sut'
HARNESS_DIR = IMPL_ROOT / 'harness'
REPO_ROOT = IMPL_ROOT.parents[1]
FREEZE_ROOT = REPO_ROOT / 'docs' / 'research' / 'sem_rev_e0' / 'freeze' / 'v1'

sys.path.insert(0, str(SUT_DIR))

import runtime  # noqa: E402
import s0_write  # noqa: E402
import s1_close  # noqa: E402
import s2_reopen  # noqa: E402
import s3_retrieve  # noqa: E402
import s4_qualify  # noqa: E402
import s5_project  # noqa: E402


def observed_runtime():
    conn = sqlite3.connect(':memory:')
    try:
        return runtime.observe_runtime(conn)
    finally:
        conn.close()


class TestRuntimeObserved(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.observed = observed_runtime()
        print('SQLITE_VERSION_RUNTIME =', cls.observed['sqlite_version'])
        print('SQLITE_SOURCE_ID_RUNTIME =', cls.observed['sqlite_source_id'])

    def test_sqlite_version_is_3_53_4(self):
        self.assertEqual(self.observed['sqlite_version'], '3.53.4')

    def test_sqlite_source_id_matches_pin(self):
        self.assertEqual(
            self.observed['sqlite_source_id'],
            runtime.EXPECTED_SQLITE_SOURCE_ID,
        )


class TestFreezeIntegrity(unittest.TestCase):
    def test_freeze_manifest_checksums(self):
        manifest_sha = (FREEZE_ROOT / 'MANIFEST.sha256').read_text(encoding='utf-8')
        for line in manifest_sha.splitlines():
            if not line.strip():
                continue
            digest, rel = line.split(None, 1)
            path = FREEZE_ROOT / rel
            self.assertTrue(path.exists(), rel)
            actual = hashlib.sha256(path.read_bytes()).hexdigest()
            self.assertEqual(actual, digest, rel)


class TestSQLiteGuards(unittest.TestCase):
    def test_version_guard_rejects_mismatch(self):
        status, value = runtime.check_runtime_values('3.45.1', runtime.EXPECTED_SQLITE_SOURCE_ID)
        self.assertEqual(status, 'version_mismatch')
        self.assertEqual(value, '3.45.1')

    def test_source_id_guard_rejects_mismatch(self):
        status, _ = runtime.check_runtime_values('3.53.4', 'not-the-pinned-source-id')
        self.assertEqual(status, 'source_id_mismatch')

    def test_matching_runtime_accepted(self):
        status, _ = runtime.check_runtime_values(
            runtime.EXPECTED_SQLITE_VERSION, runtime.EXPECTED_SQLITE_SOURCE_ID
        )
        self.assertEqual(status, 'ok')

    def test_memory_db_forbidden(self):
        with self.assertRaises(runtime.RuntimeGuardError):
            runtime.forbid_memory_db(':memory:')


class TestSchemaStrict(unittest.TestCase):
    def test_all_tables_are_strict(self):
        schema = (IMPL_ROOT / 'schema.sql').read_text(encoding='utf-8')
        creates = [ln for ln in schema.splitlines() if ln.startswith('CREATE TABLE')]
        self.assertGreaterEqual(len(creates), 8)
        self.assertEqual(schema.count('CREATE TABLE'), schema.count(') STRICT;'))

    def test_no_is_current_column(self):
        schema = (IMPL_ROOT / 'schema.sql').read_text(encoding='utf-8')
        self.assertNotIn('is_current', schema)

    def test_strict_rejects_wrong_type(self):
        with tempfile.TemporaryDirectory() as tmp:
            db = os.path.join(tmp, 't.db')
            conn = runtime.connect(db)
            s0_write.create_schema(conn)
            with self.assertRaises(sqlite3.DatabaseError):
                conn.execute(
                    "INSERT INTO entity (entity_id, entity_type, recorded_at) VALUES (?, ?, ?)",
                    (b'not-text', 'x', 't'),
                )
            conn.close()


class HarnessCase(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.cwd = os.getcwd()
        os.chdir(self.tmp.name)
        self.db = os.path.join(self.tmp.name, 'semrev_e0.db')
        os.environ['SEMREV_DB_PATH'] = self.db
        os.environ['SEMREV_QUERY_AS_OF'] = '2026-02-01T00:00:00Z'

    def tearDown(self):
        os.chdir(self.cwd)
        self.tmp.cleanup()

    def write_full(self):
        conn = s0_write.run_s0(self.db)
        conn.close()
        s1_close.run_s1(self.db)
        conn = s2_reopen.run_s2(self.db)
        conn.close()
        s3 = s3_retrieve.run_s3(self.db)
        s4 = s4_qualify.run_s4(self.db)
        s5 = s5_project.run_s5(self.db)
        return s3, s4, s5


class TestS0(HarnessCase):
    def test_file_backed_not_memory(self):
        conn = s0_write.run_s0(self.db)
        conn.close()
        self.assertTrue(os.path.isfile(self.db))
        self.assertGreater(os.path.getsize(self.db), 0)

    def test_foreign_keys_on(self):
        conn = s0_write.run_s0(self.db)
        fk = conn.execute('PRAGMA foreign_keys').fetchone()[0]
        conn.close()
        self.assertEqual(int(fk), 1)


class TestS1S2(HarnessCase):
    def test_close_reopen_persistence(self):
        conn = s0_write.run_s0(self.db)
        conn.close()
        s1_close.run_s1(self.db)
        conn = s2_reopen.run_s2(self.db)
        n = conn.execute('SELECT COUNT(*) FROM assertion').fetchone()[0]
        conn.close()
        self.assertGreaterEqual(n, 5)

    def test_new_process_s2(self):
        conn = s0_write.run_s0(self.db)
        conn.close()
        s1_close.run_s1(self.db)
        env = os.environ.copy()
        env['SEMREV_DB_PATH'] = self.db
        env['PYTHONPATH'] = str(SUT_DIR)
        result = subprocess.run(
            [sys.executable, str(SUT_DIR / 's2_reopen.py')],
            env=env,
            cwd=self.tmp.name,
            capture_output=True,
            text=True,
        )
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn('S2 REOPEN: SUCCESS', result.stdout)


class TestS3(HarnessCase):
    def test_fixture_b_alpha_beta(self):
        conn = s0_write.run_s0(self.db)
        conn.close()
        s3 = s3_retrieve.run_s3(self.db)
        ids = [c['assertion_id'] for c in s3['fixture_b']]
        self.assertIn('as:alpha-v1', ids)
        self.assertIn('as:beta-v1', ids)

    def test_fixture_c_dec_pos_1(self):
        conn = s0_write.run_s0(self.db)
        conn.close()
        s3 = s3_retrieve.run_s3(self.db)
        ids = [c['decision_id'] for c in s3['fixture_c']]
        self.assertIn('dec:pos-1', ids)

    def test_ad9_outside_candidate_membership(self):
        conn = s0_write.run_s0(self.db)
        conn.close()
        s3 = s3_retrieve.run_s3(self.db)
        b_ids = [c['assertion_id'] for c in s3['fixture_b']]
        c_ids = [c['decision_id'] for c in s3['fixture_c']]
        self.assertNotIn('dec:ad-9', b_ids)
        self.assertNotIn('dec:ad-9', c_ids)


class TestS4(HarnessCase):
    def test_fixture_a_exact_state_and_reasons(self):
        self.write_full()
        s4 = json.loads(Path('s4_output.json').read_text(encoding='utf-8'))
        a = s4['fixture_a']['assertions']
        self.assertEqual(a['as:path-a-v1']['semantic_force'], 'proposal')
        self.assertEqual(a['as:path-a-v1']['status'], 'retracted')
        self.assertEqual(a['as:path-a-v1']['rejection_reason'], 'R1_CONSTRAINT_FAILURE')
        self.assertEqual(a['as:path-b-v1']['semantic_force'], 'decision')
        self.assertEqual(a['as:path-b-v1']['status'], 'superseded')
        self.assertEqual(a['as:path-b-v1']['decision_reason'], 'R2_MEETS_K1')
        self.assertEqual(a['as:path-c-v1']['semantic_force'], 'decision')
        self.assertEqual(a['as:path-c-v1']['status'], 'current')
        self.assertEqual(a['as:path-c-v1']['decision_reason'], 'R3_NEW_REQUIREMENT_K2')
        self.assertEqual(s4['fixture_a']['current_path'], 'Path-C')
        self.assertEqual(
            s4['fixture_a']['reopen_B_requires'],
            'Y_K2_REMOVED_AND_OWNER_REAPPROVES_B',
        )

    def test_fixture_b_multi_reasons(self):
        self.write_full()
        s4 = json.loads(Path('s4_output.json').read_text(encoding='utf-8'))
        fb = s4['fixture_b']
        self.assertEqual(fb['status'], 'NO_QUALIFIED_RESULT')
        self.assertEqual(fb['qualified_assertion_ids'], [])
        by = {e.get('assertion_id') or e.get('decision_id'): e for e in fb['excluded']}
        self.assertTrue({'scope_mismatch', 'retracted', 'force_not_allowed'} <= set(by['as:alpha-v1']['reasons']))
        self.assertTrue({'scope_mismatch', 'no_approved_authority_decision'} <= set(by['as:beta-v1']['reasons']))
        self.assertIn('authority_outcome_refused', by['dec:ad-9']['reasons'])

    def test_alpha_missing_revision_fails_closed(self):
        conn = s0_write.run_s0(self.db)
        conn.execute("DELETE FROM revision WHERE revision_id = 'rev:alpha-retract'")
        conn.commit()
        conn.close()
        s3_retrieve.run_s3(self.db)
        result = s4_qualify.run_s4(self.db)
        self.assertIsNone(result)

    def test_ad9_missing_fails_closed(self):
        conn = s0_write.run_s0(self.db)
        conn.execute("DELETE FROM authority_decision WHERE decision_id = 'dec:ad-9'")
        conn.commit()
        conn.close()
        s3_retrieve.run_s3(self.db)
        result = s4_qualify.run_s4(self.db)
        self.assertIsNone(result)

    def test_evidence_record_missing_fails_closed(self):
        conn = s0_write.run_s0(self.db)
        conn.execute("DELETE FROM evidence_assertion_link")
        conn.execute("DELETE FROM evidence")
        conn.commit()
        conn.close()
        s3_retrieve.run_s3(self.db)
        result = s4_qualify.run_s4(self.db)
        self.assertIsNone(result)

    def test_evidence_link_missing_fails_closed(self):
        conn = s0_write.run_s0(self.db)
        conn.execute("DELETE FROM evidence_assertion_link WHERE assertion_id = 'as:alpha-v1'")
        conn.commit()
        conn.close()
        s3_retrieve.run_s3(self.db)
        result = s4_qualify.run_s4(self.db)
        self.assertIsNone(result)

    def test_observed_at_missing_fails_closed(self):
        conn = s0_write.run_s0(self.db)
        # STRICT NOT NULL: clear via delete+reinsert without observed_at is blocked;
        # emulate missing by nulling through a rebuild of evidence row using empty string
        # then S4 treats empty observed_at as missing.
        conn.execute("UPDATE evidence SET observed_at = '' WHERE evidence_id LIKE 'ev:%' OR 1=1")
        conn.commit()
        conn.close()
        s3_retrieve.run_s3(self.db)
        result = s4_qualify.run_s4(self.db)
        self.assertIsNone(result)

    def test_temporal_valid_from_missing_fails_closed(self):
        conn = s0_write.run_s0(self.db)
        conn.execute("UPDATE assertion SET valid_from = NULL WHERE assertion_id = 'as:alpha-v1'")
        conn.commit()
        conn.close()
        s3_retrieve.run_s3(self.db)
        result = s4_qualify.run_s4(self.db)
        self.assertIsNone(result)

    def test_revision_dependency_missing_fails_closed(self):
        conn = s0_write.run_s0(self.db)
        conn.execute("DELETE FROM revision WHERE revision_id = 'rev:A-reject'")
        conn.commit()
        conn.close()
        s3_retrieve.run_s3(self.db)
        result = s4_qualify.run_s4(self.db)
        self.assertIsNone(result)

    def test_authority_dependency_missing_fails_closed(self):
        # Keep S3 candidate membership, then remove the authority row so S4
        # fail-closes on the typed dependency rather than ordinary exclusion.
        conn = s0_write.run_s0(self.db)
        conn.close()
        s3 = s3_retrieve.run_s3(self.db)
        self.assertIsNotNone(s3)
        import runtime as _rt
        conn = _rt.connect(self.db, must_exist=True)
        conn.execute("DELETE FROM authority_decision WHERE decision_id = 'dec:pos-1'")
        conn.commit()
        conn.close()
        result = s4_qualify.run_s4(self.db)
        self.assertIsNone(result)

    def test_declared_loss_preserved(self):
        self.write_full()
        s4 = json.loads(Path('s4_output.json').read_text(encoding='utf-8'))
        by = {e.get('assertion_id'): e for e in s4['fixture_b']['excluded'] if e.get('assertion_id')}
        self.assertEqual(by['as:alpha-v1']['declared_loss'], 1)
        self.assertEqual(by['as:beta-v1']['declared_loss'], 1)

    def test_derived_currentness_not_stored_flag(self):
        conn = s0_write.run_s0(self.db)
        cols = [r[1] for r in conn.execute('PRAGMA table_info(assertion)').fetchall()]
        conn.close()
        self.assertNotIn('is_current', cols)
        s3_retrieve.run_s3(self.db)
        s4 = s4_qualify.run_s4(self.db)
        self.assertTrue(s4['fixture_a']['assertions']['as:path-c-v1']['currentness'])
        self.assertFalse(s4['fixture_a']['assertions']['as:path-a-v1']['currentness'])

    def test_unknown_discipline(self):
        self.write_full()
        s4 = json.loads(Path('s4_output.json').read_text(encoding='utf-8'))
        a = s4['fixture_a']['assertions']['as:path-a-v1']
        self.assertEqual(a['uncertainty'], 'UNKNOWN')
        self.assertEqual(a['reopen_requires'], 'UNKNOWN')


class TestS5(HarnessCase):
    def test_exact_byte_sha(self):
        _, _, s5 = self.write_full()
        on_disk = Path('s5_output.json').read_bytes()
        digest = hashlib.sha256(on_disk).hexdigest()
        self.assertEqual(s5['sha256'], digest)
        line = Path('s5_output.sha256').read_text(encoding='utf-8')
        self.assertTrue(line.endswith('\n'))
        self.assertEqual(line.strip().split()[0], digest)
        proj = json.loads(on_disk.decode('utf-8'))
        self.assertNotIn('database_path', proj.get('s5_projection', {}))

    def test_s5_deterministic_across_temp_dirs(self):
        """Same semantic state in different temp dirs => identical S5 bytes/hash."""
        digests = []
        payloads = []
        for _ in range(2):
            with tempfile.TemporaryDirectory() as tmp:
                cwd = os.getcwd()
                try:
                    os.chdir(tmp)
                    db = os.path.join(tmp, 'semrev_e0.db')
                    os.environ['SEMREV_DB_PATH'] = db
                    os.environ['SEMREV_QUERY_AS_OF'] = '2026-02-01T00:00:00Z'
                    conn = s0_write.run_s0(db)
                    conn.close()
                    s1_close.run_s1(db)
                    conn = s2_reopen.run_s2(db)
                    conn.close()
                    s3_retrieve.run_s3(db)
                    s4_qualify.run_s4(db)
                    s5 = s5_project.run_s5(db)
                    data = Path('s5_output.json').read_bytes()
                    payloads.append(data)
                    digests.append(s5['sha256'])
                    self.assertNotIn(b'database_path', data)
                    self.assertNotIn(tmp.encode(), data)
                finally:
                    os.chdir(cwd)
        self.assertEqual(payloads[0], payloads[1])
        self.assertEqual(digests[0], digests[1])

class TestOracleIsolation(HarnessCase):
    def test_oracle_unavailable_before_s5_hash(self):
        env = os.environ.copy()
        result = subprocess.run(
            [sys.executable, str(HARNESS_DIR / 'scorer.py')],
            env=env,
            cwd=self.tmp.name,
            capture_output=True,
            text=True,
        )
        self.assertNotEqual(result.returncode, 0)
        combined = result.stdout + result.stderr
        self.assertIn('oracle unavailable before s5 hash', combined.lower())

    def test_sut_does_not_import_harness(self):
        for path in SUT_DIR.glob('*.py'):
            tree = ast.parse(path.read_text(encoding='utf-8'))
            for node in ast.walk(tree):
                if isinstance(node, ast.Import):
                    for alias in node.names:
                        self.assertFalse(alias.name.startswith('harness'))
                if isinstance(node, ast.ImportFrom) and node.module:
                    self.assertFalse(node.module.startswith('harness'))


class TestScorer(HarnessCase):
    def test_required_forbidden_behavior(self):
        self.write_full()
        result = subprocess.run(
            [sys.executable, str(HARNESS_DIR / 'scorer.py')],
            cwd=self.tmp.name,
            capture_output=True,
            text=True,
        )
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        payload = json.loads(Path('scorer_output.json').read_text(encoding='utf-8'))
        self.assertTrue(payload['scorer_pass'])
        self.assertEqual(payload['forbidden_hits'], [])
        self.assertFalse(payload['core_result_produced'])
        self.assertTrue(payload.get('oracle_atoms_complete'))
        self.assertIn('subject=ent:service:orion', payload['required_ok'])
        self.assertIn('authority=principal:release-board', payload['required_ok'])


class TestNoPlaceholders(unittest.TestCase):
    def test_no_unconditional_assert_true(self):
        src = Path(__file__).read_text(encoding='utf-8')
        self.assertNotIn('assertTrue' + '(True)', src)


class TestPipelineIntegration(unittest.TestCase):
    def test_implementation_only_integration(self):
        env = os.environ.copy()
        result = subprocess.run(
            [sys.executable, str(IMPL_ROOT / 'run_pipeline.py')],
            env=env,
            cwd=str(IMPL_ROOT),
            capture_output=True,
            text=True,
        )
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn('S0 WRITE: SUCCESS', result.stdout)
        self.assertIn('S1 CLOSE: SUCCESS', result.stdout)
        self.assertIn('S2 REOPEN: SUCCESS', result.stdout)
        self.assertIn('S3 RETRIEVE: SUCCESS', result.stdout)
        self.assertIn('S4 QUALIFY: SUCCESS', result.stdout)
        self.assertIn('S5 PROJECT: SUCCESS', result.stdout)
        self.assertIn('Scoring Harness: SUCCESS', result.stdout)
        self.assertIn('IMPLEMENTATION_TEST_ONLY', result.stdout)
        self.assertNotIn('SEM_REV_E0_CORE_PASS', result.stdout)


if __name__ == '__main__':
    unittest.main()
