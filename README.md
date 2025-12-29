# Rate Limiter Service (Sliding Window Algorithm)

A backend **Rate Limiting Service** built using **FastAPI** that enforces per-user request limits using a **Sliding Window** algorithm.

This project demonstrates core **backend system design concepts** such as request throttling, in-memory data structures, and API-level protection.

---

## 🚀 Features

- Per-user rate limiting
- Sliding window algorithm (time-based)
- FastAPI middleware-style integration
- Clear separation of logic (limiter vs API)
- Deterministic behavior with timestamps
- HTTP 429 response on limit breach

---

## 🧠 How It Works (Sliding Window)

For each user:
- Maintain a list of request timestamps
- On every request:
  1. Remove timestamps older than the time window
  2. Check remaining count
  3. Allow or block the request

Example:
- Limit: **4 requests per 60 seconds**
- Only timestamps inside the last 60 seconds are counted

---

## 🛠 Tech Stack

- **Python**
- **FastAPI**
- **Uvicorn**

---

## 📂 Project Structure

- rate-limiter/ 
    - main.py # FastAPI app and routes
    - limiter.py # Sliding window rate limiting logic
    - requirements.txt
    - README.md


---

## ▶️ How to Run Locally

```bash
# Create virtual environment
python -m venv .venv
source .venv/bin/activate   # Mac/Linux

# Install dependencies
pip install -r requirements.txt

# Run server
uvicorn main:app --reload
