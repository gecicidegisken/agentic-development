# agentic-development

Project
-------
A minimal Flask web application: a blue-themed single-page calculator for learning and quick experimentation. The app is intentionally small and demonstrates a Flask entry point, a simple UI, and unit tests for core arithmetic logic.

Features
--------
- Single-page calculator UI served at / with operations: add, subtract, multiply, divide, and clear
- Minimal Flask app entry point (app.py)
- Core arithmetic utilities in divider.py with unit tests (test_divider.py)
- Static assets and template in static/ and templates/

Requirements
------------
- Python 3.7 or newer
- Recommended: use a virtual environment (venv)

Setup
-----
1. Create and activate a virtual environment (recommended):

   python3 -m venv venv
   source venv/bin/activate  # macOS / Linux
   venv\Scripts\activate    # Windows (PowerShell: venv\Scripts\Activate.ps1)

2. Install the required dependency (Flask):

   python3 -m pip install Flask

Running the app
---------------
Start the application with:

   python3 app.py

By default the app listens on http://127.0.0.1:5000 and serves a single page at / (the calculator UI).

Running tests
-------------
Run the test suite with pytest:

   python3 -m pytest -q

or

   pytest

The tests exercise functions in test_divider.py which validate the arithmetic utilities in divider.py.

Project structure
-----------------
- app.py             - Flask application entry point that serves the calculator page
- divider.py         - Core arithmetic helpers (e.g. divide)
- templates/         - HTML templates (index.html)
- static/            - CSS and other static assets (blue-themed styles)
- test_divider.py    - Pytest tests for divider.py
- README.md          - This file

Contributing
------------
Contributions are welcome. To contribute:

1. Fork the repository.
2. Create a branch for your change: git checkout -b feature/my-change
3. Make your changes and add/update tests as appropriate.
4. Open a pull request describing your change.

Please reference ClickUp task id: 86ey773kb in PRs related to this work and follow conventional commit messages (for example: `docs: improve README`).

License
-------
This repository does not include a formal license file. It is provided for learning and experimentation. Add a LICENSE file if you need to set a usage license.

Author
------
Maintainer: project repository owner

Contact: open an issue or submit a pull request on the repository

Notes
-----
The app is a minimal, blue-themed Flask calculator that serves a single page at / with add/subtract/multiply/divide/clear operations. Default URL: http://127.0.0.1:5000

