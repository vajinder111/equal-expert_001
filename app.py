from fastapi import FastAPI
import httpx

app = FastAPI()

@app.get("/{user}")
async def get_gists(user: str) -> Dict[str, Any]:
    url = f"https://api.github.com/users/{user}/gists"
    resp = await get(url)
    resp.raise_for_status()
    return {"user": user, "public_gists": resp.json()}  # Wrap as dict!
