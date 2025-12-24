import time
from collections import defaultdict

# configuration
REQUEST_LIMIT = 5
WINDOW_SIZE =  10 # seconds

# in-memory store
user_requests = defaultdict(list)


def is_request_allowed(user_id: str) -> bool:
    now = time.time()

    timestamps = user_requests[user_id]

    # remove timestamps older than window
    valid_timestamps = [
        ts for ts in timestamps if now - ts < WINDOW_SIZE
    ]

    user_requests[user_id] = valid_timestamps

    if len(valid_timestamps) >= REQUEST_LIMIT:
        return False

    # allow request
    user_requests[user_id].append(now)
    return True

def get_user_status(user_id: str):
    now = time.time()

    timestamps = user_requests[user_id]
    valid_timestamps = [
        ts for ts in timestamps if now - ts < WINDOW_SIZE
    ]

    user_requests[user_id] = valid_timestamps

    remaining = REQUEST_LIMIT - len(valid_timestamps)

    if valid_timestamps:
        reset_in = WINDOW_SIZE - (now - min(valid_timestamps))
    else:
        reset_in = WINDOW_SIZE

    return {
        "used": len(valid_timestamps),
        "remaining": max(0, remaining),
        "reset_in_seconds": int(reset_in)
    }
