from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import time

from limiter import is_request_allowed
from limiter import is_request_allowed, get_user_status


app = FastAPI()


class RequestData(BaseModel):
    user_id: str


@app.post("/request")
def handle_request(data: RequestData):
    allowed = is_request_allowed(data.user_id)

    if not allowed:
        raise HTTPException(status_code=429, detail="Rate limit exceeded")

    return {"status": "allowed"}

@app.get("/status/{user_id}")
def get_status(user_id: str):
    return get_user_status(user_id)
