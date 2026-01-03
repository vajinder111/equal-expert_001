# Gists API

## Local Setup
1. `pip install -r requirements.txt`
2. `uvicorn app:app --host 0.0.0.0 --port 8080 --reload`
3. Test: `curl http://localhost:8080/octocat`
4. Run tests: `pytest`

## Docker
`docker build -t gists-api . && docker run -p 8080:8080 gists-api`

Endpoint: GET /<user> returns public gists JSON.
