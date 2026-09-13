-- SEM-REV-E0 v1 Schema
-- SQLite 3.53.4 required
-- STRICT tables, explicit PKs, foreign keys ON

PRAGMA foreign_keys = ON;
PRAGMA journal_mode = WAL;

-- Entity table
CREATE TABLE IF NOT EXISTS entity (
    entity_id TEXT PRIMARY KEY,
    entity_type TEXT NOT NULL,
    recorded_at TEXT NOT NULL
);

-- Scope table
CREATE TABLE IF NOT EXISTS scope (
    scope_id TEXT PRIMARY KEY,
    description TEXT
);

-- Semantic force enum
CREATE TABLE IF NOT EXISTS semantic_force (
    force_id TEXT PRIMARY KEY,
    description TEXT NOT NULL
);

-- Uncertainty enum
CREATE TABLE IF NOT EXISTS uncertainty (
    uncertainty_id TEXT PRIMARY KEY,
    description TEXT NOT NULL
);

-- Authority table
CREATE TABLE IF NOT EXISTS authority (
    authority_id TEXT PRIMARY KEY,
    authority_type TEXT NOT NULL
);

-- Source table
CREATE TABLE IF NOT EXISTS source (
    source_id TEXT PRIMARY KEY,
    source_type TEXT NOT NULL,
    description TEXT
);

-- Assertion table
CREATE TABLE IF NOT EXISTS assertion (
    assertion_id TEXT PRIMARY KEY,
    entity_id TEXT NOT NULL,
    semantic_force TEXT NOT NULL,
    scope_id TEXT NOT NULL,
    content TEXT,
    asserted_at TEXT NOT NULL,
    recorded_at TEXT NOT NULL,
    valid_from TEXT,
    valid_to TEXT,
    uncertainty TEXT,
    declared_loss BOOLEAN DEFAULT FALSE,
    FOREIGN KEY (entity_id) REFERENCES entity(entity_id),
    FOREIGN KEY (semantic_force) REFERENCES semantic_force(force_id),
    FOREIGN KEY (scope_id) REFERENCES scope(scope_id),
    FOREIGN KEY (uncertainty) REFERENCES uncertainty(uncertainty_id)
);

-- Evidence table
CREATE TABLE IF NOT EXISTS evidence (
    evidence_id TEXT PRIMARY KEY,
    source_id TEXT NOT NULL,
    observed_at TEXT NOT NULL,
    recorded_at TEXT NOT NULL,
    description TEXT,
    FOREIGN KEY (source_id) REFERENCES source(source_id)
);

-- Evidence-Assertion link
CREATE TABLE IF NOT EXISTS evidence_assertion_link (
    evidence_id TEXT NOT NULL,
    assertion_id TEXT NOT NULL,
    PRIMARY KEY (evidence_id, assertion_id),
    FOREIGN KEY (evidence_id) REFERENCES evidence(evidence_id),
    FOREIGN KEY (assertion_id) REFERENCES assertion(assertion_id)
);

-- Revision table
CREATE TABLE IF NOT EXISTS revision (
    revision_id TEXT PRIMARY KEY,
    revision_type TEXT NOT NULL,
    target_assertion_id TEXT NOT NULL,
    replacement_assertion_id TEXT,
    reason TEXT NOT NULL,
    effective_from TEXT NOT NULL,
    recorded_at TEXT NOT NULL,
    FOREIGN KEY (target_assertion_id) REFERENCES assertion(assertion_id),
    FOREIGN KEY (replacement_assertion_id) REFERENCES assertion(assertion_id)
);

-- Authority decision table
CREATE TABLE IF NOT EXISTS authority_decision (
    decision_id TEXT PRIMARY KEY,
    assertion_id TEXT,
    authority_id TEXT NOT NULL,
    outcome TEXT NOT NULL,
    semantic_force TEXT NOT NULL,
    scope_id TEXT NOT NULL,
    reason TEXT,
    effective_from TEXT NOT NULL,
    recorded_at TEXT NOT NULL,
    FOREIGN KEY (assertion_id) REFERENCES assertion(assertion_id),
    FOREIGN KEY (authority_id) REFERENCES authority(authority_id),
    FOREIGN KEY (semantic_force) REFERENCES semantic_force(force_id),
    FOREIGN KEY (scope_id) REFERENCES scope(scope_id)
);

-- Trace table (for audit)
CREATE TABLE IF NOT EXISTS trace (
    trace_id TEXT PRIMARY KEY,
    operation TEXT NOT NULL,
    entity_type TEXT NOT NULL,
    entity_id TEXT NOT NULL,
    timestamp TEXT NOT NULL,
    details TEXT
);

-- Qualified projection (S5 output)
CREATE TABLE IF NOT EXISTS qualified_projection (
    projection_id TEXT PRIMARY KEY,
    assertion_id TEXT NOT NULL,
    is_qualified BOOLEAN NOT NULL,
    reason TEXT,
    currentness BOOLEAN NOT NULL,
    authority_status TEXT,
    uncertainty TEXT,
    declared_loss BOOLEAN DEFAULT FALSE,
    FOREIGN KEY (assertion_id) REFERENCES assertion(assertion_id),
    FOREIGN KEY (uncertainty) REFERENCES uncertainty(uncertainty_id)
);

-- Indexes for performance
CREATE INDEX IF NOT EXISTS idx_assertion_entity ON assertion(entity_id);
CREATE INDEX IF NOT EXISTS idx_assertion_force ON assertion(semantic_force);
CREATE INDEX IF NOT EXISTS idx_assertion_scope ON assertion(scope_id);
CREATE INDEX IF NOT EXISTS idx_assertion_valid ON assertion(valid_from, valid_to);
CREATE INDEX IF NOT EXISTS idx_revision_target ON revision(target_assertion_id);
CREATE INDEX IF NOT EXISTS idx_revision_type ON revision(revision_type);
CREATE INDEX IF NOT EXISTS idx_authority_decision_outcome ON authority_decision(outcome);
CREATE INDEX IF NOT EXISTS idx_authority_decision_scope ON authority_decision(scope_id);
