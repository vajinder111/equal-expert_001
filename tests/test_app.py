import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pytest
from fastapi.testclient import TestClient
from app import app

client = TestClient(app)


def test_octocat_gists():
    resp = client.get("/octocat")
    assert resp.status_code == 200
    data = resp.json()
    assert data["user"] == "octocat"
    assert "public_gists" in data
    gists = data["public_gists"]
    assert len(gists) >= 5  # curl output
