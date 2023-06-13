# hse-algo

## Usage

```console
# activating venv
poetry shell

# on first run
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser

# run server
python manage.py runserver
```

## Installation

```console
pip install poetry

# requires python3.10
poetry install --without dev
```

## Hooks & tests

```console
# require installation with dev
make format && make test
```
