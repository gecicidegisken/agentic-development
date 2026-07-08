# agentic-development

A minimal Flask-based calculator web app and small utility module for dividing and averaging numbers. This repository is intended as a compact example project for local development, testing, and exploration.

Table of contents
- Project overview
- Features
- Prerequisites
- Installation
- Running the app locally
- Testing
- Project structure
- Contributing
- Troubleshooting (common errors)
- Contact & credits

Project overview

This project contains a small Flask application that serves a single web page at the root route (`/`) and a tiny utility module (divider.py) that implements basic numeric helpers (divide and average). The web UI is served from the templates and static folders, while the Python logic and tests live at the repository root.

Features

- Simple Flask app serving a single page at `/` (index route)
- Basic numeric utilities:
  - divide(a, b): returns a / b or None on division by zero
  - average(numbers): returns the arithmetic mean of a list, or None if unable to compute
- Unit tests validating the divide and average behaviour

Prerequisites

- Python 3.7+ (python3 command available)
- pip (Python package installer)
- Optional but recommended: virtualenv/venv for an isolated environment

Installation

1. (Optional) Create and activate a virtual environment

On macOS / Linux:

python3 -m venv venv
source venv/bin/activate

On Windows (PowerShell):

python3 -m venv venv
venv\Scripts\Activate.ps1

2. Install Flask (only dependency required to run the web app)

python3 -m pip install Flask

Running the app locally

Start the Flask development server with the included app entrypoint:

python3 app.py

This runs the Flask app in debug mode and listens on http://127.0.0.1:5000. Open that URL in your browser to view the single-page UI served by templates/index.html.

Notes about the web app
- The route / is defined in app.py as a single endpoint "index" which returns render_template('index.html').
- Static assets and templates are located in the static/ and templates/ directories respectively.

Testing

This repo includes unit tests for the divider utilities in test_divider.py. The tests are written using Python's built-in unittest framework but can be executed with pytest if you prefer.

Run tests with unittest (built-in):

python3 -m unittest test_divider.py -v

Or run with pytest (pytest will discover and run unittest-style tests):

python3 -m pytest test_divider.py -q

What the tests cover
- divide(): correct division for normal inputs, and returning None when dividing by zero
- average(): correct mean calculation and returning None for empty input

Project structure (brief)

- app.py: Minimal Flask application. Defines the '/' route which renders the index template and runs the app when executed directly.
- divider.py: Core calculator logic used by tests (divide and average functions). Contains a small main() that demonstrates usage.
- templates/: HTML template(s) for the web UI (index.html is rendered by app.py).
- static/: Static files (CSS, JS, images) used by the frontend.
- test_divider.py: Unit tests for the functions in divider.py using unittest.
- README.md: This file.

Contributing

Contributions are welcome. Typical steps to contribute:
- Fork the repository and create a feature branch
- Run and extend tests locally
- Open a pull request with a clear description of your change

Please follow these guidelines when contributing code:
- Keep changes minimal and focused
- Add or update tests for behavior changes
- Do not commit secrets or environment-specific configuration

Troubleshooting (common errors)

1) sqlite3.OperationalError: unable to open database file (or similar)

Context: This repository is a minimal Flask app and does not include a database by default. If you see an sqlite3 OperationalError when running tests or other tooling, it usually means some component (a third-party extension, a local script, or CI job) attempted to open a SQLite database file but could not find it or lacked permissions.

Steps to debug:
- Confirm whether your code or a dependency actually uses sqlite3. Search the repo for "sqlite3" or for code that opens a .db file.
- If an external tool or test is trying to use a DB, inspect the path it attempts to open. Relative paths are resolved from the current working directory, so run the same command and print the CWD (for example, add a short Python snippet that prints os.getcwd()).
- Check file permissions where the DB file should live. Ensure the executing user can read/write the directory.
- If migrations or schema setup are required, run the commands needed to create the DB or tables (this repo does not provide migrations; create the file manually or run the initialization steps for your app/tooling).
- Use the sqlite3 CLI to inspect or create a database for debugging:

# open an interactive sqlite shell
sqlite3 my_test.db
# inside sqlite3 prompt, list tables
.tables
# run a quick pragma to check schema
PRAGMA table_info(your_table_name);

- In Python you can also test connection quickly:

python3 - <<'PY'
import sqlite3
conn = sqlite3.connect('my_test.db')
print('OK:', conn)
conn.close()
PY

2) "name '_git_parsed' is not defined" or similar NameError from external tooling

Context: This error is not raised by the code in this repository. It indicates some external integration, script, or CI job expects a variable/fixture named _git_parsed to exist but it is missing.

Steps to debug:
- Search the repository (and CI/config files if available) for occurrences of _git_parsed to find the integration point.
- If the error appears in CI, inspect pipeline scripts or automation steps that run before your test or app execution; the missing variable may be set by a helper script that failed or by a missing plugin.
- Reproduce locally: run the exact command used in the failing environment to see the full traceback. Example:

# If CI runs `python3 -m pytest`, run the same locally:
python3 -m pytest -q

- Read the traceback top-to-bottom. The file and line that raises NameError identifies where the undefined name is referenced.
- Ensure all required initialization or context providers (fixtures, environment variables, pre-test steps) have been executed.
- If the variable should be created by a script, run that script manually to see why it might not have produced _git_parsed.

General debugging tips
- Re-run the failing command locally with increased verbosity to capture full stack traces.
- Print or log the current working directory and environment variables that may affect file paths or tool behavior.
- Use git to check if missing files are present in the branch you are testing.

Contact & credits

This repository contains small example code and tests intended for demonstration and practice. If you need help understanding the code or testing it locally, open an issue in the project repository with details about your environment and the full error trace.

License

The code in this repository is provided as-is for educational purposes. No license file is included.

---

If you notice any inaccuracies in this README relative to the repository contents, please report them in an issue so the documentation can be corrected.

