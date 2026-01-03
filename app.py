from fastapi import FastAPI
import httpx  # Change to sync import
from typing import Dict, Any

app = FastAPI()

@app.get("/{user}")
def get_gists(user: str) -> Dict[str, Any]:  # Remove 'async'
    url = f"https://api.github.com/users/{user}/gists"
    resp = httpx.get(url)  # Sync call now
    resp.raise_for_status()
    return {"user": user, "public_gists": resp.json()}
