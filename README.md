# Essence Demo
A cryptocurrency dashboard with a form and table viz with data provided by Alpaca API and login via GitHub OAuth2.0

## System Requirements

The project uses poetry for Python to create an isolated environment and manage package dependencies. To prepare your system, ensure you have an official distribution of Python version 3.9+ and install poetry using one of the following commands (as instructed by the [poetry documentation](https://python-poetry.org/docs/#system-requirements)):

### Poetry installation (Bash)

```bash
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python
```

### Poetry installation (PowerShell)

```powershell
(Invoke-WebRequest -Uri https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py -UseBasicParsing).Content | python
```

## Dependencies

The project uses a virtual environment to isolate package dependencies. To create the virtual environment and install required packages, run the following from your preferred shell:

```bash
$ poetry install
```

You'll also need to clone a new `.env` file from the `.env.template` to store local configuration options. This is a one-time operation on first setup:

```bash
$ cp .env.template .env  # (first time only)
```

The `.env` file is used by flask to set environment variables when running `flask run`. This enables things like development mode (which also enables features like hot reloading when you make a file change). There's also a [SECRET_KEY](https://flask.palletsprojects.com/en/1.1.x/config/#SECRET_KEY) variable which is used to encrypt the flask session cookie.

## Running the App

Once the all dependencies have been installed, start the Flask app in development mode within the poetry environment by running:
```bash
$ poetry run flask run
```

You should see output similar to the following:
```bash
 * Serving Flask app 'essence_demo/app' (lazy loading)
 * Environment: development
 * Debug mode: on
 * Running on http://127.0.0.1:5000 (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 144-764-892
```
Now visit [`http://localhost:5000/`](http://localhost:5000/) in your web browser to view the app.

## GitHub OAuth2.0

For login create a [GitHub OAuth App](https://docs.github.com/en/developers/apps/building-oauth-apps/creating-an-oauth-app). Set the following fields:
- Homepage URL - `http://localhost:5000`
- Authorization callback URL - `http://localhost:5000/login/callback`


## Future changes
- [ ] Testable Component Design/architecture
- [ ] Presentation and service logic layers (HTTP calls, app flow, shared data)
- [ ] Form handling with validation
- [ ] Table sorting and pagination. Maybe use [DataTables.js](https://blog.miguelgrinberg.com/post/beautiful-interactive-tables-for-your-flask-templates) or [Dash inside Flask](https://hackersandslackers.com/plotly-dash-with-flask/)
- [ ] Unit and integration tests a minimum, with BDD tests using tools like Cypress would be good to see but not essential
- [ ] Add static typing, and pre-commit hooks etc
- [ ] List of allowed users
