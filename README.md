# FlowGuard 

FlowGuard is a backend **API Rate Limiting Service** that enforces per-user request limits using a **sliding window algorithm**.

## Features
- Per-user rate limiting (4 requests per 60 seconds)
- Sliding window algorithm for accurate time-based limiting
- HTTP 429 responses when limits are exceeded
- Status endpoint to inspect usage and reset time
- Clean separation between API layer and core logic

## Tech Stack
- Python
- FastAPI
- Uvicorn

## How It Works
For each user, FlowGuard tracks timestamps of recent requests.
On every request:
1. Old timestamps outside the time window are removed
2. Remaining requests are counted
3. If the limit is exceeded, the request is rejected

## API Endpoints

### POST `/request`
Checks whether a request is allowed.

Request body:
```json
{
  "user_id": "kapil"
}
