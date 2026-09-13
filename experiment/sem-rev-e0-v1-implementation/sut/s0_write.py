#!/usr/bin/env python3
"""
S0 WRITE - Write all frozen records to SQLite database
FROZEN SPEC: SEM-REV-E0 v1

Requirements:
- file-backed SQLite only
- STRICT tables
- explicit primary keys
- stable application semantic IDs
- typed mandatory qualifiers
- explicit relationships
- explicit transactions
- PRAGMA foreign_keys=ON on every connection
- no :memory:
- no rowid semantic identity
- no free mutable "is_current"

MUST NOT persist:
- REQUIRED expected atoms
- FORBIDDEN expected atoms
- expected result labels
- gold projection
- equivalent answer key
"""

import sqlite3
import os
import sys
from datetime import datetime, timezone

DB_PATH = os.environ.get('SEMREV_DB_PATH', 'semrev_e0.db')


def get_connection(db_path=DB_PATH):
    """Get SQLite connection with required pragmas"""
    conn = sqlite3.connect(db_path)
    conn.execute('PRAGMA foreign_keys = ON')
    conn.execute('PRAGMA journal_mode = WAL')
    conn.execute('PRAGMA strict = ON')

    # Verify SQLite version
    version = conn.execute('SELECT sqlite_version()').fetchone()[0]
    if version != '3.53.4':
        print(f'ERROR: SQLite version mismatch. Expected 3.53.4, got {version}')
        conn.close()
        sys.exit(1)

    source_id = conn.execute('SELECT sqlite_source_id()').fetchone()[0]
    expected_source_id = '2026-07-24 19:02:57 bf7c7f30031888f4e796e429ab3978879485813aaca6f641c7b33e4e09459bcc'
    if source_id != expected_source_id:
        print(f'ERROR: SQLite source ID mismatch')
        conn.close()
        sys.exit(1)

    return conn


def create_schema(conn):
    """Create database schema"""
    with open('schema.sql', 'r') as f:
        schema = f.read()
    conn.executescript(schema)
    conn.commit()


def insert_reference_data(conn):
    """Insert reference data (enums)"""
    now = datetime.now(timezone.utc).isoformat()

    forces = [
        ('proposal', 'Proposal'),
        ('claim', 'Claim'),
        ('observation', 'Observation'),
        ('decision', 'Decision'),
        ('authority_decision', 'Authority Decision'),
    ]
    conn.executemany(
        'INSERT OR IGNORE INTO semantic_force (force_id, description) VALUES (?, ?)',
        forces
    )

    uncertainties = [
        ('preliminary_unblinded_two_runs', 'Preliminary unblinded two runs'),
        ('twelve_runs_summary_only', 'Twelve runs summary only'),
    ]
    conn.executemany(
        'INSERT OR IGNORE INTO uncertainty (uncertainty_id, description) VALUES (?, ?)',
        uncertainties
    )

    scopes = [
        ('scope:project-delta', 'Project Delta'),
        ('scope:production-us', 'Production US'),
        ('scope:production-eu', 'Production EU'),
        ('scope:lab-a', 'Lab A'),
    ]
    conn.executemany(
        'INSERT OR IGNORE INTO scope (scope_id, description) VALUES (?, ?)',
        scopes
    )

    authorities = [
        ('principal:release-board', 'Release Board'),
        ('principal:project-owner', 'Project Owner'),
    ]
    conn.executemany(
        'INSERT OR IGNORE INTO authority (authority_id, authority_type) VALUES (?, ?)',
        authorities
    )

    sources = [
        ('src:lab-a', 'Lab A'),
        ('src:release-board', 'Release Board'),
    ]
    conn.executemany(
        'INSERT OR IGNORE INTO source (source_id, source_type, description) VALUES (?, ?, ?)',
        [(s[0], s[1], s[1]) for s in sources]
    )

    conn.commit()


def insert_fixture_a(conn):
    """Insert Fixture A data"""
    now = datetime.now(timezone.utc).isoformat()
    recorded_at = now

    conn.execute(
        'INSERT OR IGNORE INTO entity (entity_id, entity_type, recorded_at) VALUES (?, ?, ?)',
        ('ent:project:delta', 'project', recorded_at)
    )

    conn.execute(
        """INSERT INTO assertion
           (assertion_id, entity_id, semantic_force, scope_id, content,
            asserted_at, recorded_at, valid_from, valid_to, uncertainty, declared_loss)
           VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, FALSE)""",
        ('as:path-a-v1', 'ent:project:delta', 'proposal', 'scope:project-delta',
         'Path-A proposal', '2026-01-01T00:00:00Z', recorded_at, '2026-01-01T00:00:00Z',
         None, None, None)
    )

    conn.execute(
        """INSERT INTO assertion
           (assertion_id, entity_id, semantic_force, scope_id, content,
            asserted_at, recorded_at, valid_from, valid_to, uncertainty, declared_loss)
           VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, FALSE)""",
        ('as:path-b-v1', 'ent:project:delta', 'decision', 'scope:project-delta',
         'Path-B decision', '2026-01-03T00:00:00Z', recorded_at, '2026-01-03T00:00:00Z',
         None, None, None)
    )

    conn.execute(
        """INSERT INTO assertion
           (assertion_id, entity_id, semantic_force, scope_id, content,
            asserted_at, recorded_at, valid_from, valid_to, uncertainty, declared_loss)
           VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, FALSE)""",
        ('as:path-c-v1', 'ent:project:delta', 'decision', 'scope:project-delta',
         'Path-C decision', '2026-01-04T00:00:00Z', recorded_at, '2026-01-04T00:00:00Z',
         None, None, None)
    )

    conn.execute(
        """INSERT INTO revision
           (revision_id, revision_type, target_assertion_id, replacement_assertion_id,
            reason, effective_from, recorded_at)
           VALUES (?, ?, ?, ?, ?, ?, ?)""",
        ('rev:A-reject', 'retracts', 'as:path-a-v1', None,
         'R1_CONSTRAINT_FAILURE', '2026-01-02T00:00:00Z', recorded_at)
    )

    conn.execute(
        """INSERT INTO revision
           (revision_id, revision_type, target_assertion_id, replacement_assertion_id,
            reason, effective_from, recorded_at)
           VALUES (?, ?, ?, ?, ?, ?, ?)""",
        ('rev:B-to-C', 'supersedes', 'as:path-b-v1', 'as:path-c-v1',
         'R3_NEW_REQUIREMENT_K2', '2026-01-04T00:00:00Z', recorded_at)
    )

    conn.commit()


def insert_fixture_b(conn):
    """Insert Fixture B data"""
    now = datetime.now(timezone.utc).isoformat()
    recorded_at = now

    conn.execute(
        'INSERT OR IGNORE INTO entity (entity_id, entity_type, recorded_at) VALUES (?, ?, ?)',
        ('ent:service:atlas', 'service', recorded_at)
    )

    conn.execute(
        """INSERT INTO assertion
           (assertion_id, entity_id, semantic_force, scope_id, content,
            asserted_at, recorded_at, valid_from, valid_to, uncertainty, declared_loss)
           VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, FALSE)""",
        ('as:alpha-v1', 'ent:service:atlas', 'claim', 'scope:lab-a',
         'Lab-A claim ~40% p50 reduction', '2026-01-01T00:00:00Z', recorded_at,
         '2026-01-01T00:00:00Z', '2026-01-14T00:00:00Z',
         'preliminary_unblinded_two_runs', False)
    )

    conn.execute(
        """INSERT INTO assertion
           (assertion_id, entity_id, semantic_force, scope_id, content,
            asserted_at, recorded_at, valid_from, valid_to, uncertainty, declared_loss)
           VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, FALSE)""",
        ('as:beta-v1', 'ent:service:atlas', 'observation', 'scope:lab-a',
         '12 Lab-A runs observed 7.8% median p50 reduction', '2026-01-01T00:00:00Z', recorded_at,
         '2026-01-01T00:00:00Z', '2026-01-14T00:00:00Z',
         'twelve_runs_summary_only', False)
    )

    conn.execute(
        """INSERT INTO authority_decision
           (decision_id, assertion_id, authority_id, outcome, semantic_force,
            scope_id, reason, effective_from, recorded_at)
           VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)""",
        ('dec:ad-9', None, 'principal:release-board', 'refused', 'authority_decision',
         'scope:production-us', 'ONLY_PRELIMINARY_LAB_A_EVIDENCE',
         '2026-01-15T00:00:00Z', recorded_at)
    )

    conn.execute(
        """INSERT INTO revision
           (revision_id, revision_type, target_assertion_id, replacement_assertion_id,
            reason, effective_from, recorded_at)
           VALUES (?, ?, ?, ?, ?, ?, ?)""",
        ('rev:alpha-retract', 'retracts', 'as:alpha-v1', None,
         'INSUFFICIENT_FOR_AUTHORIZATION', '2026-01-14T00:00:00Z', recorded_at)
    )

    conn.commit()


def insert_fixture_c(conn):
    """Insert Fixture C data (positive control)"""
    now = datetime.now(timezone.utc).isoformat()
    recorded_at = now

    conn.execute(
        'INSERT OR IGNORE INTO entity (entity_id, entity_type, recorded_at) VALUES (?, ?, ?)',
        ('ent:service:orion', 'service', recorded_at)
    )

    conn.execute(
        """INSERT INTO authority_decision
           (decision_id, assertion_id, authority_id, outcome, semantic_force,
            scope_id, reason, effective_from, recorded_at)
           VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)""",
        ('dec:pos-1', None, 'principal:release-board', 'approved', 'authority_decision',
         'scope:production-eu', 'RELEASE_CRITERIA_MET',
         '2026-01-20T00:00:00Z', recorded_at)
    )

    conn.commit()


def main():
    print('S0 WRITE: Starting...')

    db_path = os.environ.get('SEMREV_DB_PATH', 'semrev_e0.db')
    if db_path == ':memory:' or 'memory' in db_path.lower():
        print('ERROR: :memory: database is forbidden')
        sys.exit(1)

    conn = get_connection(db_path)

    try:
        create_schema(conn)

        insert_reference_data(conn)

        insert_fixture_a(conn)
        insert_fixture_b(conn)
        insert_fixture_c(conn)

        conn.commit()

        print(f'S0 WRITE: Database created at {db_path}')
        print('S0 WRITE: SUCCESS')

    finally:
        conn.close()


if __name__ == '__main__':
    main()
