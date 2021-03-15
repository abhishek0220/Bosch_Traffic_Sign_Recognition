# Bosch_Traffic_Sign_Recognition

[![Python 3.7](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/release/python-370/)
  
# Instructions to Run locally and contribute [Windows]
1. Install [Python](https://www.python.org/downloads/).
2. Clone this repository and open terminal, change directory to the repo.
3. Run `python -m venv venv` to create virtual environment.
4. Run `venv\Scripts\activate` command to activate virtual environment.
5. Run `pip install -r reqirements.txt` command to install dependencies.
7. Create System Var `$env:FLASK_APP="application.py"`, `$env:FLASK_DEBUG=1` using terminal.
8. Enter `flask run` to create server.

# Instructions to Run locally and contribute [Linux]
1. Install [Python](https://www.python.org/downloads/).
2. Clone this repository and open terminal, change directory to the repo.
3. Run `python -m venv venv` to create virtual environment.
4. Run `venv\bin\activate` command to activate virtual environment.
5. Run `pip install -r reqirements.txt` command to install dependencies.
7. Create System Var `export FLASK_APP="application.py"`, `export FLASK_DEBUG=1` using terminal.
8. Enter `flask run` to create server.

Make sure to run `pip freeze > requirements.txt` after installing any new package


