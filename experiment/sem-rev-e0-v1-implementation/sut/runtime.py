#!/usr/bin/env python3
"""
Shared SQLite runtime guards for SEM-REV-E0 v1 implementation.
IMPLEMENTATION_TEST_ONLY — not experimental evidence.
"""

import os
import sqlite3
import sys

EXPECTED_SQLITE_VERSION = '3.53.4'
EXPECTED_SQLITE_SOURCE_ID = (
    '2026-07-24 19:02:57 '
    'bf7c7f30031888f4e796e429ab3978879485813aaca6f641c7b33e4e09459bcc'
)

QUERY_AS_OF_DEFAULT = '2026-02-01T00:00:00Z'


class RuntimeGuardError(Exception):
    pass


def impl_root():
    return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def schema_path():
    cwd_schema = os.path.join(os.getcwd(), 'schema.sql')
    if os.path.exists(cwd_schema):
        return cwd_schema
    return os.path.join(impl_root(), 'schema.sql')


def forbid_memory_db(db_path):
    if db_path is None:
        raise RuntimeGuardError('database path is required')
    lowered = str(db_path).lower()
    if db_path == ':memory:' or lowered.startswith('file:mem'):
        print('ERROR: :memory: database is forbidden')
        raise RuntimeGuardError(':memory: database is forbidden')
    if lowered == 'memory' or lowered.endswith(':memory:'):
        print('ERROR: :memory: database is forbidden')
        raise RuntimeGuardError(':memory: database is forbidden')


def observe_runtime(conn):
    version = conn.execute('SELECT sqlite_version()').fetchone()[0]
    source_id = conn.execute('SELECT sqlite_source_id()').fetchone()[0]
    return {
        'sqlite_version': version,
        'sqlite_source_id': source_id,
    }


def check_runtime_values(version, source_id):
    """Pure comparison used by mismatch tests. Does not touch a live connection."""
    if version != EXPECTED_SQLITE_VERSION:
        return ('version_mismatch', version)
    if source_id != EXPECTED_SQLITE_SOURCE_ID:
        return ('source_id_mismatch', source_id)
    return ('ok', version)


def enforce_runtime(conn):
    observed = observe_runtime(conn)
    status, _ = check_runtime_values(
        observed['sqlite_version'], observed['sqlite_source_id']
    )
    if status == 'version_mismatch':
        print(
            f"ERROR: SQLite version mismatch. Expected {EXPECTED_SQLITE_VERSION}, "
            f"got {observed['sqlite_version']}"
        )
        raise RuntimeGuardError('SQLite version mismatch')
    if status == 'source_id_mismatch':
        print('ERROR: SQLite source ID mismatch')
        raise RuntimeGuardError('SQLite source ID mismatch')
    return observed


def connect(db_path, must_exist=False):
    forbid_memory_db(db_path)
    if must_exist and not os.path.exists(db_path):
        print(f'ERROR: Database file not found at {db_path}')
        raise RuntimeGuardError(f'Database file not found at {db_path}')
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    conn.execute('PRAGMA foreign_keys = ON')
    conn.execute('PRAGMA journal_mode = WAL')
    try:
        enforce_runtime(conn)
    except RuntimeGuardError:
        conn.close()
        raise
    fk = conn.execute('PRAGMA foreign_keys').fetchone()[0]
    if int(fk) != 1:
        conn.close()
        print('ERROR: foreign_keys is not ON')
        raise RuntimeGuardError('foreign_keys is not ON')
    return conn


def fail_exit(exc):
    if isinstance(exc, RuntimeGuardError):
        sys.exit(1)
    print(f'ERROR: {exc}')
    sys.exit(1)
