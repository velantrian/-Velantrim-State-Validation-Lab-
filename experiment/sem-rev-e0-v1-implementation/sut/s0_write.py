#!/usr/bin/env python3
"""
S0 WRITE - Write all frozen records to SQLite database
FROZEN SPEC: SEM-REV-E0 v1
IMPLEMENTATION_TEST_ONLY
"""

import os
import sys

from runtime import connect, fail_exit, schema_path, RuntimeGuardError


def create_schema(conn):
    path = schema_path()
    with open(path, 'r', encoding='utf-8') as f:
        schema = f.read()
    conn.executescript(schema)
    conn.commit()


def insert_reference_data(conn):
    recorded_at = '2026-01-01T00:00:00Z'
    conn.executemany(
        'INSERT OR IGNORE INTO semantic_force (force_id, description) VALUES (?, ?)',
        [
            ('proposal', 'Proposal'),
            ('claim', 'Claim'),
            ('observation', 'Observation'),
            ('decision', 'Decision'),
            ('authority_decision', 'Authority Decision'),
        ],
    )
    conn.executemany(
        'INSERT OR IGNORE INTO uncertainty (uncertainty_id, description) VALUES (?, ?)',
        [
            ('preliminary_unblinded_two_runs', 'Preliminary unblinded two runs'),
            ('twelve_runs_summary_only', 'Twelve runs summary only'),
        ],
    )
    conn.executemany(
        'INSERT OR IGNORE INTO scope (scope_id, description) VALUES (?, ?)',
        [
            ('scope:project-delta', 'Project Delta'),
            ('scope:production-us', 'Production US'),
            ('scope:production-eu', 'Production EU'),
            ('scope:lab-a', 'Lab A'),
        ],
    )
    conn.executemany(
        'INSERT OR IGNORE INTO authority (authority_id, authority_type) VALUES (?, ?)',
        [
            ('principal:release-board', 'Release Board'),
            ('principal:project-owner', 'Project Owner'),
        ],
    )
    conn.executemany(
        'INSERT OR IGNORE INTO source (source_id, source_type, description) VALUES (?, ?, ?)',
        [
            ('src:lab-a', 'lab', 'Lab A'),
            ('src:release-board', 'authority', 'Release Board'),
            ('src:project-owner', 'authority', 'Project Owner'),
        ],
    )
    for eid, etype in (
        ('ent:project:delta', 'project'),
        ('ent:service:atlas', 'service'),
        ('ent:service:orion', 'service'),
    ):
        conn.execute(
            'INSERT OR IGNORE INTO entity (entity_id, entity_type, recorded_at) VALUES (?, ?, ?)',
            (eid, etype, recorded_at),
        )
    conn.commit()


def insert_fixture_a(conn):
    recorded_at = '2026-01-04T00:00:00Z'
    conn.execute(
        """INSERT INTO assertion
           (assertion_id, entity_id, semantic_force, scope_id, content, reason,
            reopen_requires, asserted_at, recorded_at, valid_from, valid_to,
            uncertainty, declared_loss)
           VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
        ('as:path-a-v1', 'ent:project:delta', 'proposal', 'scope:project-delta',
         'Path-A', None, None,
         '2026-01-01T00:00:00Z', recorded_at, '2026-01-01T00:00:00Z',
         None, None, 0),
    )
    conn.execute(
        """INSERT INTO assertion
           (assertion_id, entity_id, semantic_force, scope_id, content, reason,
            reopen_requires, asserted_at, recorded_at, valid_from, valid_to,
            uncertainty, declared_loss)
           VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
        ('as:path-b-v1', 'ent:project:delta', 'decision', 'scope:project-delta',
         'Path-B', 'R2_MEETS_K1', 'Y_K2_REMOVED_AND_OWNER_REAPPROVES_B',
         '2026-01-03T00:00:00Z', recorded_at, '2026-01-03T00:00:00Z',
         None, None, 0),
    )
    conn.execute(
        """INSERT INTO assertion
           (assertion_id, entity_id, semantic_force, scope_id, content, reason,
            reopen_requires, asserted_at, recorded_at, valid_from, valid_to,
            uncertainty, declared_loss)
           VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
        ('as:path-c-v1', 'ent:project:delta', 'decision', 'scope:project-delta',
         'Path-C', 'R3_NEW_REQUIREMENT_K2', None,
         '2026-01-04T00:00:00Z', recorded_at, '2026-01-04T00:00:00Z',
         None, None, 0),
    )
    conn.execute(
        """INSERT INTO revision
           (revision_id, revision_type, target_assertion_id, replacement_assertion_id,
            reason, effective_from, recorded_at)
           VALUES (?, ?, ?, ?, ?, ?, ?)""",
        ('rev:A-reject', 'retracts', 'as:path-a-v1', None,
         'R1_CONSTRAINT_FAILURE', '2026-01-02T00:00:00Z', recorded_at),
    )
    conn.execute(
        """INSERT INTO revision
           (revision_id, revision_type, target_assertion_id, replacement_assertion_id,
            reason, effective_from, recorded_at)
           VALUES (?, ?, ?, ?, ?, ?, ?)""",
        ('rev:B-to-C', 'supersedes', 'as:path-b-v1', 'as:path-c-v1',
         'R3_NEW_REQUIREMENT_K2', '2026-01-04T00:00:00Z', recorded_at),
    )
    conn.execute(
        """INSERT INTO authority_decision
           (decision_id, assertion_id, authority_id, outcome, semantic_force,
            scope_id, reason, effective_from, recorded_at)
           VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)""",
        ('dec:path-b-owner', 'as:path-b-v1', 'principal:project-owner', 'approved',
         'authority_decision', 'scope:project-delta', 'R2_MEETS_K1',
         '2026-01-03T00:00:00Z', recorded_at),
    )
    conn.execute(
        """INSERT INTO authority_decision
           (decision_id, assertion_id, authority_id, outcome, semantic_force,
            scope_id, reason, effective_from, recorded_at)
           VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)""",
        ('dec:path-c-owner', 'as:path-c-v1', 'principal:project-owner', 'approved',
         'authority_decision', 'scope:project-delta', 'R3_NEW_REQUIREMENT_K2',
         '2026-01-04T00:00:00Z', recorded_at),
    )
    conn.commit()


def insert_fixture_b(conn):
    recorded_at = '2026-01-15T00:00:00Z'
    conn.execute(
        """INSERT INTO assertion
           (assertion_id, entity_id, semantic_force, scope_id, content, reason,
            reopen_requires, asserted_at, recorded_at, valid_from, valid_to,
            uncertainty, declared_loss)
           VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
        ('as:alpha-v1', 'ent:service:atlas', 'claim', 'scope:lab-a',
         'Lab-A claim ~40% p50 reduction', None, None,
         '2026-01-01T00:00:00Z', recorded_at,
         '2026-01-01T00:00:00Z', None,
         'preliminary_unblinded_two_runs', 1),
    )
    conn.execute(
        """INSERT INTO assertion
           (assertion_id, entity_id, semantic_force, scope_id, content, reason,
            reopen_requires, asserted_at, recorded_at, valid_from, valid_to,
            uncertainty, declared_loss)
           VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
        ('as:beta-v1', 'ent:service:atlas', 'observation', 'scope:lab-a',
         '12 Lab-A runs observed 7.8% median p50 reduction', None, None,
         '2026-01-01T00:00:00Z', recorded_at,
         '2026-01-01T00:00:00Z', None,
         'twelve_runs_summary_only', 1),
    )
    conn.execute(
        """INSERT INTO authority_decision
           (decision_id, assertion_id, authority_id, outcome, semantic_force,
            scope_id, reason, effective_from, recorded_at)
           VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)""",
        ('dec:ad-9', None, 'principal:release-board', 'refused', 'authority_decision',
         'scope:production-us', 'ONLY_PRELIMINARY_LAB_A_EVIDENCE',
         '2026-01-15T00:00:00Z', recorded_at),
    )
    conn.execute(
        """INSERT INTO revision
           (revision_id, revision_type, target_assertion_id, replacement_assertion_id,
            reason, effective_from, recorded_at)
           VALUES (?, ?, ?, ?, ?, ?, ?)""",
        ('rev:alpha-retract', 'retracts', 'as:alpha-v1', None,
         'INSUFFICIENT_FOR_AUTHORIZATION', '2026-01-14T00:00:00Z', recorded_at),
    )
    conn.execute(
        """INSERT INTO evidence
           (evidence_id, source_id, observed_at, recorded_at, description, declared_loss)
           VALUES (?, ?, ?, ?, ?, ?)""",
        ('ev:alpha-v1', 'src:lab-a', '2026-01-10T00:00:00Z', recorded_at,
         'raw logs/blinding record absent', 1),
    )
    conn.execute(
        """INSERT INTO evidence
           (evidence_id, source_id, observed_at, recorded_at, description, declared_loss)
           VALUES (?, ?, ?, ?, ?, ?)""",
        ('ev:beta-v1', 'src:lab-a', '2026-01-12T00:00:00Z', recorded_at,
         'run-level data absent', 1),
    )
    conn.execute(
        'INSERT INTO evidence_assertion_link (evidence_id, assertion_id) VALUES (?, ?)',
        ('ev:alpha-v1', 'as:alpha-v1'),
    )
    conn.execute(
        'INSERT INTO evidence_assertion_link (evidence_id, assertion_id) VALUES (?, ?)',
        ('ev:beta-v1', 'as:beta-v1'),
    )
    conn.commit()


def insert_fixture_c(conn):
    recorded_at = '2026-01-20T00:00:00Z'
    conn.execute(
        """INSERT INTO authority_decision
           (decision_id, assertion_id, authority_id, outcome, semantic_force,
            scope_id, reason, effective_from, recorded_at)
           VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)""",
        ('dec:pos-1', None, 'principal:release-board', 'approved', 'authority_decision',
         'scope:production-eu', 'RELEASE_CRITERIA_MET',
         '2026-01-20T00:00:00Z', recorded_at),
    )
    conn.commit()


def run_s0(db_path):
    conn = connect(db_path, must_exist=False)
    try:
        create_schema(conn)
        insert_reference_data(conn)
        insert_fixture_a(conn)
        insert_fixture_b(conn)
        insert_fixture_c(conn)
        conn.commit()
        print(f'S0 WRITE: Database created at {db_path}')
        print('S0 WRITE: SUCCESS')
        return conn
    except Exception:
        conn.close()
        raise


def main():
    print('S0 WRITE: Starting...')
    db_path = os.environ.get('SEMREV_DB_PATH', 'semrev_e0.db')
    try:
        conn = run_s0(db_path)
        conn.close()
    except RuntimeGuardError as e:
        fail_exit(e)
    except Exception as e:
        print(f'S0 WRITE: ERROR - {e}')
        sys.exit(1)


if __name__ == '__main__':
    main()
