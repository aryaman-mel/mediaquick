from app import app
import json

def test_index():
    client = app.test_client()
    r = client.get("/")
    assert r.status_code == 200
    # ensure your page loads – check something you expect in index.html
    assert b"<!DOCTYPE html" in r.data or b"<html" in r.data

def test_interactions_endpoint():
    client = app.test_client()
    payload = {"medicines": ["aspirin", "ibuprofen"]}
    r = client.post("/interactions", data=json.dumps(payload), content_type="application/json")
    assert r.status_code == 200
    data = r.get_json()
    assert "interactions" in data
    # you hard-coded aspirin/ibuprofen → bleeding risk
    notes = [i["note"] for i in data["interactions"]]
    assert any("bleeding" in n.lower() for n in notes)
