# Flask Web App

Simple Flask application that showcases project cards with search, category filtering, modal details, a contact form, and light/dark theme toggling.

## Features

- Project listing with search and category filter
- JSON endpoint for item details
- Contact form with server-side validation and flash messages
- Theme toggle persisted in session
- Responsive Bootstrap UI
- Unit tests with pytest
- GitHub Actions CI (lint + startup check + tests)

## Tech Stack

- Python 3.10+
- Flask 3.0.0
- Werkzeug 3.0.1
- Bootstrap 5
- Jinja2
- pytest

## Project Structure

~~~text
WebApp/
├── .github/
│   └── workflows/
│       └── python-app.yml
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── about.html
│   └── contact.html
├── tests/
│   └── test_app.py
├── app.py
├── requirements.txt
└── README.md
~~~

## Run Locally

1. Create and activate a virtual environment.

~~~bash
python -m venv .venv
source .venv/bin/activate
~~~

2. Install dependencies.

~~~bash
pip install -r requirements.txt
~~~

3. Start the app.

~~~bash
python app.py
~~~

4. Open http://localhost:5000

## Environment Variables

- SECRET_KEY: Recommended for stable session security in development/production.
- FLASK_DEBUG: Set to 1 to enable Flask debug mode.

Example:

~~~bash
export SECRET_KEY="change-me"
export FLASK_DEBUG=1
python app.py
~~~

## Testing

Run tests:

~~~bash
pytest -q
~~~

## CI Pipeline

GitHub Actions workflow runs on push/pull request to main and includes:

- Dependency installation
- flake8 lint checks
- App startup smoke test
- pytest test suite

## License

MIT License. See LICENSE.

