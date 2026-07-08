# Agentic Development — Blue Calculator

A minimal Flask-based blue-themed calculator web app and small utility module for division/averaging. This repository is a lightweight demo intended for learning, quick experiments, and onboarding new contributors.

Table of Contents

- [Features](#features)
- [Project Structure](#project-structure)
- [Prerequisites](#prerequisites)
- [Local setup](#local-setup)
- [Running the app](#running-the-app)
- [Testing](#testing)
- [Usage](#usage)
- [Development notes](#development-notes)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [License](#license)
- [Contact / Author](#contact--author)
- [ClickUp task](#clickup-task)


Features

- Small Flask web app serving a single calculator UI (index.html).
- Client-side JavaScript calculator logic with a blue theme (static/styles.css).
- A tiny utility module (divider.py) with divide and average functions and unit tests (test_divider.py).
- Designed to be simple and easy to fork for experimentation.


Project Structure

A brief file tree and purpose of the most important files:

- app.py — Flask app entry point. Serves templates/index.html on `/`.
- templates/index.html — The calculator UI and client-side JavaScript.
- static/styles.css — Styles for the blue-themed calculator.
- divider.py — Python utility functions: divide(a, b) and average(numbers). Contains a simple main() demo.
- test_divider.py — Unit tests for divide and average (unittest style). Runable with pytest or python -m unittest.
- README.md — (this file) project documentation and development guide.


Prerequisites

- Python 3.8+ (python3 in PATH)
- pip (Python package installer)
- Optional: virtualenv or venv for isolated environments


Local setup

1. Create and activate a virtual environment (recommended):

```bash
python3 -m venv .venv
# macOS / Linux
source .venv/bin/activate
# Windows (PowerShell)
.\.venv\Scripts\Activate.ps1
```

2. Install dependencies (Flask is the only required package for the web app):

```bash
python3 -m pip install --upgrade pip
python3 -m pip install Flask
```

Note: If you plan to run tests with pytest you can install it as well:

```bash
python3 -m pip install pytest
```


Running the app

Start the Flask development server from the repository root:

```bash
python3 app.py
```

By default app.py runs in debug mode and binds to:

- Host: 127.0.0.1 (localhost)
- Port: 5000

Open your browser at: http://127.0.0.1:5000

When running in debug mode, changes to templates and static files will be picked up automatically.


Testing

You can run the unit tests for the divider utility in a few ways. From the repository root:

- Using pytest (recommended if installed):

```bash
pytest -q test_divider.py
# or to run only this test file with python -m pytest
python3 -m pytest -q test_divider.py
```

- Using the standard library unittest runner:

```bash
python3 -m unittest test_divider.py
```

Expected tests cover:
- divide(a, b) returning a float for valid division and None for division by zero.
- average(numbers) returning the mean or None for empty lists.


Usage

1. Start the app (see Running the app).
2. Open http://127.0.0.1:5000 in your browser.
3. Use the on-screen buttons to build expressions and evaluate them.

Example interactions:

- Basic: 2 + 3 = → displays 5
- Multiply: 7 * 6 = → displays 42
- Parentheses & exponent: ( 2 + 3 ) ^ 2 = → displays 25 (the UI shows ^ but uses JavaScript ** under the hood)
- Square root: √ 9 ) = → inserts Math.sqrt(9) and evaluates to 3 (note: the UI inserts Math.sqrt( and you must close the parenthesis before evaluating)

Notes:
- The calculator evaluates expressions client-side using JavaScript's Function(...) evaluator. This is minimal and suitable for this demo but not for untrusted input in production.


Development notes

- Templates and static assets:
  - Edit templates/index.html to change UI markup or client-side behavior.
  - Edit static/styles.css to adjust styling and theming.
  - The Flask dev server (app.py) runs with debug=True so template and static changes are auto-reloaded.

- Python code:
  - divider.py contains divide() and average(). Update tests in test_divider.py when changing behavior.

- Adding dependencies:
  - If you add new Python packages, update any project documentation and consider adding a requirements.txt.


Troubleshooting

- Flask not found / ImportError:
  - Ensure your virtualenv is activated and Flask is installed:

```bash
python3 -m pip install Flask
```

- Port 5000 already in use:
  - Either stop the process using that port or modify app.run(...) in app.py to use a different port, e.g. app.run(host='127.0.0.1', port=5001, debug=True)

- Tests failing unexpectedly:
  - Confirm you are running tests from the repository root and using python3.
  - Run a single test file for clearer output:

```bash
python3 -m pytest -q test_divider.py
```

- Browser shows "Error" after evaluating an expression:
  - The calculator uses a JS evaluator; malformed expressions or unclosed parentheses will trigger an error and reset the input.


Contributing

Thanks for wanting to contribute! A simple workflow:

1. Fork the repository and create a feature branch:
   - Branch naming suggestion: feat/xxx, fix/xxx, docs/xxx, chore/xxx
2. Make small, focused commits. Suggested commit message prefixes (Conventional-style):
   - feat: add new feature
   - fix: bug fix
   - docs: documentation only changes
   - chore: maintenance tasks
3. Run tests locally before opening a PR:

```bash
pytest -q
```

4. Open a pull request with a clear description of changes and link to related ClickUp task(s) if applicable.


License

This repository does not include a LICENSE file. If you want to apply a license, a common choice is the MIT License. Add a LICENSE file at project root if needed and update this section accordingly.


Contact / Author

- Maintainers: Please add the project maintainer or team contact here.
- For issues, open an issue or a PR in the repository.


ClickUp task

- ClickUp: https://app.clickup.com/t/86ey773kb
- Task ID: 86ey773kb

Replace the link and ID above with the real ClickUp task URL and identifier for traceability.

Repository

- Replace this with the canonical remote repository URL (e.g. https://github.com/your-org/your-repo)


Thank you for reading — happy hacking!

