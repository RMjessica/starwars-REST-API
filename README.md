# Star Wars REST API :rocket:

## Features

- Integrated with Pipenv for package managing.
- SQLAlchemy integration for database abstraction.

## Installation

```sh
pipenv install;
mysql -u root -e "CREATE DATABASE example";
pipenv run init;
pipenv run migrate;
pipenv run upgrade;
```

# Manual Installation for Ubuntu & Mac

⚠️ Make sure you have `python 3.6+` and `MySQL` installed on your computer and MySQL is running, then run the following commands:
```sh
$ pipenv install (to install pip packages)
$ pipenv run migrate (to create the database)
$ pipenv run start (to start the flask webserver)
```
