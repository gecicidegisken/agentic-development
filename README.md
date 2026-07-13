# agentic-development

Usage
-----

This workspace includes a minimal Flask-based blue-themed calculator web app.

To run the app locally:

1. (Optional) Create a virtual environment and activate it.
2. Install Flask if you don't have it: python3 -m pip install Flask
3. Run: python3 app.py
4. Open your browser at: http://127.0.0.1:5000

The app serves a single page at `/` with basic operations: add, subtract, multiply, divide, and clear.

Web Calculator
--------------

Run locally with: python3 app.py
Open: http://127.0.0.1:5000/
Supports parentheses, %, and ^ (maps to exponent). √ inserts Math.sqrt().
Security: expressions are evaluated client-side and are not safe for
untrusted input.

