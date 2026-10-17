import json
import re

SC1_VERSION = "sc1-structured-basis-v1"
LEDGER_TRANSFORM_VERSION = "source-bound-ledger-v1"
VALID_STATUSES = {"SUPPORTED", "HYPOTHESIS", "UNKNOWN", "REJECTED"}

def normalize_sc1(declared_qualification, basis_world_status):
    d = str(declared_qualification).strip().upper()
    b = str(basis_world_status).strip().upper()
    if d not in VALID_STATUSES or b not in VALID_STATUSES:
        return {"consistency_status":"UNSCORABLE","normalized_qualification":"UNSCORABLE","normalization_rule_version":SC1_VERSION}
    if d == b:
        return {"consistency_status":"CONSISTENT","normalized_qualification":d,"normalization_rule_version":SC1_VERSION}
    if {d,b} == {"SUPPORTED","REJECTED"}:
        return {"consistency_status":"SEMANTIC_CONFLICT_UNRESOLVED","normalized_qualification":"UNSCORABLE","normalization_rule_version":SC1_VERSION}
    if "SUPPORTED" in {d,b}: normalized = "SUPPORTED"
    elif "REJECTED" in {d,b}: normalized = "REJECTED"
    elif "HYPOTHESIS" in {d,b}: normalized = "HYPOTHESIS"
    else: normalized = "UNKNOWN"
    return {"consistency_status":"SEMANTIC_CONFLICT_RESOLVED","normalized_qualification":normalized,"normalization_rule_version":SC1_VERSION}

def public_fixture_projection(record):
    return {
        "fixture_id": record["fixture_id"],
        "model_visible_source": record["model_visible_source"],
        "model_visible_relation_candidate": record["model_visible_relation_candidate"],
    }

def _relation_type(candidate):
    m = re.match(r"^([A-Z_]+)\(", str(candidate).strip())
    return m.group(1) if m else "UNKNOWN"

def build_source_bound_ledger(public_fixture, schema):
    source = public_fixture["model_visible_source"]
    candidate = public_fixture["model_visible_relation_candidate"]
    relation_type = _relation_type(candidate)
    missing = []
    for field in schema["fields"]:
        if relation_type not in field.get("relation_types", []):
            continue
        negative = any(re.search(p, source, re.I) for p in field.get("negative_patterns", []))
        positive = any(re.search(p, source, re.I) for p in field.get("positive_patterns", []))
        if negative or not positive:
            missing.append({"field_id":field["field_id"],"status":"NOT_PROVIDED_BY_SOURCE"})
    missing.sort(key=lambda x: x["field_id"])
    return {
        "ledger_version": LEDGER_TRANSFORM_VERSION,
        "fixture_id": public_fixture["fixture_id"],
        "relation_candidate": candidate,
        "relation_type": relation_type,
        "MISSING_SOURCE_FIELDS": missing,
    }

def canonical_json(obj):
    return json.dumps(obj, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
