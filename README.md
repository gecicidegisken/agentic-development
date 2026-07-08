# agentic-development

A minimal Flask-based calculator web application designed for learning and quick experimentation.

Project overview
----------------
This repository contains a small web app built with Flask that serves a single-page calculator. It's intended as a lightweight example for learning Flask, simple web UIs, and basic Python unit testing.

Key features
------------
- Single-page calculator UI (add, subtract, multiply, divide, clear)
- Minimal Flask app (app.py)
- Core arithmetic utilities in divider.py with unit tests (test_divider.py)
- Simple HTML/CSS assets under templates/ and static/

ClickUp task
------------
This change relates to ClickUp task id: 86ey773kb. Please reference this ID in the related pull request.

Prerequisites
-------------
- Python 3.7+ installed
- Recommended: virtual environment (venv)

Installation
------------
1. Create and activate a virtual environment (recommended):

   python3 -m venv venv
   source venv/bin/activate  # macOS / Linux
   venv\Scripts\activate     # Windows (PowerShell: venv\Scripts\Activate.ps1)

2. Install Flask:

   python3 -m pip install Flask

Running the app
---------------
Start the Flask app locally with:

python3 app.py

Then open your browser and navigate to:

http://127.0.0.1:5000

The app serves one route ('/') that renders the calculator UI.

Testing
-------
Run the test suite using pytest:

python3 -m pytest -q

or

pytest

The included tests cover functions in divider.py.

Project structure
-----------------
Top-level files and directories:

- app.py         - Minimal Flask application that serves the calculator page
- divider.py     - Core arithmetic helpers (divide, average)
- templates/     - HTML templates (index.html)
- static/        - Static assets (CSS, images, JS if any)
- test_divider.py - Pytest tests for divider.py
- README.md      - This file

Development
-----------
- To run the app during development, start it with `python3 app.py`. The app runs on 127.0.0.1:5000 by default.
- To run tests after making changes, use `pytest` or `python3 -m pytest -q`.
- To extend the calculator: add new helper functions in divider.py (or new modules), add corresponding tests in test_divider.py, and update templates/index.html or static assets as needed.

Contributing
------------
1. Fork the repository.
2. Create a feature branch: `git checkout -b feature/my-change`.
3. Make changes, include or update tests.
4. Open a pull request. Reference ClickUp task id 86ey773kb in the PR description.

Please follow conventional commits for commit messages. Example for this documentation change:

    docs: improve README with comprehensive guide

License
-------
This project is provided as-is for learning and experimentation. No specific license file is included; add a LICENSE if required for your use.

Contact
-------
For questions or issues, open an issue or submit a pull request on the repository.

