# agentic-development

A small Flask-based demo app that serves a blue-themed calculator UI and a tiny utility module for basic numeric operations. The repository is intended as a minimal example for local development, testing, and quick experimentation.

ClickUp task: 86ey773kb (When creating the PR include `#86ey773kb` in the body)

---

Prerequisites
-------------

- Python 3.8+ recommended (3.10/3.11 are fine). Verify with:

  ```bash
  python3 --version
  ```

- A virtual environment is strongly recommended (venv or virtualenv).

Setup and install
-----------------

1. Create and activate a virtual environment:

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate    # macOS / Linux
   .\.venv\Scripts\activate   # Windows (PowerShell)
   ```

2. Install Flask (only required dependency for running the web app):

   ```bash
   python3 -m pip install --upgrade pip
   python3 -m pip install Flask
   ```

Running the app locally
-----------------------

Start the Flask app with:

```bash
python3 app.py
```

Then open your browser at: http://127.0.0.1:5000

App explanation
---------------

- app.py: Creates a Flask application and registers a single route `/` which renders the calculator UI from `templates/index.html`. The application runs on host 127.0.0.1 and port 5000 by default. For local development the file starts the app with debug=True (so auto-reload and debug tracebacks are enabled).

  Route summary:
  - GET `/` -> renders templates/index.html (calculator UI)

- templates/index.html: A small single-page calculator UI with client-side JavaScript to handle input and evaluation. The UI supports digits, basic operators (+, -, *, /), parentheses, exponentiation (^ displayed, ** used under the hood for JS), modulo, and a square-root button which inserts Math.sqrt( ).

- static/: contains the stylesheet used by the UI.

How the code modules relate
--------------------------

- divider.py: a tiny utility module providing:
  - divide(a, b): returns a / b or None if division by zero occurs.
  - average(numbers): returns the arithmetic mean or None for empty lists.

The unit tests exercise these functions (see below).

Running tests
-------------

Run the unit tests included in the repo with:

```bash
python3 -m unittest test_divider.py
```

What the tests cover:
- test_divide_success: verifies `divide` returns correct floats for normal divisions.
- test_divide_by_zero: verifies `divide` returns None for zero-division attempts.
- test_average_success: verifies `average` computes correct means for non-empty lists.
- test_average_empty: verifies `average` returns None for an empty list.

Project structure
-----------------

- app.py              - Flask application and route definitions (serves `/`).
- divider.py          - Utility functions: divide(a, b) and average(numbers).
- templates/          - HTML templates; `index.html` is the calculator UI served by app.py.
- static/             - Static assets (CSS) used by the UI.
- test_divider.py     - Unit tests for divider.py using Python's unittest.
- README.md           - This file.

Development notes
-----------------

- Debug mode: app.py runs Flask with debug=True for local development. Disable debug in production.
- Port and host: Default host is 127.0.0.1 and port 5000. To run on a different port, set the FLASK_RUN_PORT environment variable or modify the app.run call in app.py.
- Next steps / improvements to consider:
  - Add CLI or API endpoints for divider functions.
  - Improve input validation and robust expression parsing for the UI (avoid using eval/Function for untrusted input).
  - Add more unit tests and CI integration.

Contribution guide
------------------

Thank you for contributing! Please follow these guidelines:

- Fork the repository and work on a feature branch for each change.
- Use clear, focused commits. Follow Conventional Commits for messages. Examples:
  - feat(calc): add exponent operator
  - fix(divider): handle float divisors correctly
  - docs(readme): improve setup instructions

- Create a pull request with a descriptive title and include the ClickUp task id and `#86ey773kb` in the PR body.

License
-------

This project is available under a placeholder license. Replace with your preferred license (e.g., MIT) before publishing.

---

If you need help, open an issue or contact the maintainers.

