import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pytest
from fastapi.testclient import TestClient
from app import app  # Now imports cleanly

client = TestClient(app)

def test_octocat_gists():
    resp = client.get("/octocat")
    assert resp.status_code == 200
    data = resp.json()
    assert data["user"] == "octocat"  # Top-level user key
    assert "public_gists" in data     # Your response key
    gists = data["public_gists"]
    assert isinstance(gists, list)    # Array of gists
    assert len(gists) > 0             # Has gists

