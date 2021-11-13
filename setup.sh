#!/bin/bash

# Installing Pipenv
echo "Installing Pipenv"
pip install --user pipenv

# Setup venv folder and setup environment
mkdir .venv
pipenv shell

pipenv install

# django setup
python manage.py makemigrations safety
python manage.py migrate

python manage.py runserver




