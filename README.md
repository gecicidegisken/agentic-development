# agentic-development

A tiny library that provides some simple arithmetic helper functions.

## Install

```bash
pip install -r requirements.txt
```

## Run the server

The project now includes a minimal HTTP API built with **FastAPI**. To start the server locally, run:

```bash
uvicorn api:app --reload
```

The server will be available at `http://127.0.0.1:8000`.

## Endpoints

- **GET `/health`** – Health‑check endpoint returning JSON `{ "status": "ok" }` with HTTP 200.
- **GET `/`** – A simple HTML page with a button that triggers the health‑check when clicked.

You can open a browser and navigate to `http://127.0.0.1:8000` to see the button. Clicking it will call the `/health` endpoint and display the JSON response.

## Running the tests

The original unit tests for the core library are located in `test_divider.py`. A new test suite `test_api.py` verifies the health‑check endpoint.

```bash
pytest -q
```

Both the original tests and the new API test should pass.

---

## Core library (`divider.py`)

```python

def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return None


def average(numbers):
    try:
        total = sum(numbers)
        return total / len(numbers)
    except ZeroDivisionError:
        return None


def main():
    values = [10, 20, 30]

    print("Average:", average(values))

    # ai should fix this
    result = divide(100, 0)

    print("Result:", result)


if __name__ == "__main__":
    main()
```

---

## API (`api.py`)

```python
from fastapi import FastAPI
from fastapi.responses import HTMLResponse, JSONResponse

app = FastAPI()

HTML_PAGE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Health Check Trigger</title>
    <script>
        async function triggerHealth() {
            const resp = await fetch('/health');
            const data = await resp.json();
            document.getElementById('result').textContent = JSON.stringify(data);
        }
    </script>
</head>
<body>
    <h1>Health‑check Trigger</h1>
    <button onclick="triggerHealth()">Check Health</button>
    <pre id="result"></pre>
</body>
</html>
"""


@app.get("/", response_class=HTMLResponse)
def root():
    """Serve a simple HTML page with a button to call the health endpoint."""
    return HTML_PAGE


@app.get("/health", response_class=JSONResponse)
def health():
    """Health‑check endpoint returning a static JSON payload."""
    return {"status": "ok"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("api:app", host="127.0.0.1", port=8000, reload=True)
```

---

## Tests (`test_api.py`)

```python
import pytest
from fastapi.testclient import TestClient
from api import app

client = TestClient(app)


def test_health_endpoint():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}
```

---

## Requirements (`requirements.txt`)

```
fastapi
uvicorn[standard]
httpx
```

---

Feel free to explore the repository, extend the API, or integrate the core library functions into new endpoints.
