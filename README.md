# Setup Instructions

Install Pipenv
```sh
pip install --user pipenv

# Make venv and start pipenv
mkdir .venv
pipenv shell

# install dependancies
pipenv install


# Django Comands
python manage.py makemigrations safety
python manage.py migrate
python manage.py runserver
```
Runs on localhost:8000
