# hse-algo

## Usage

### Running in container

```console
make build
make run

# now server is running at 127.0.0.1:8000
# to stop:
make stop

# to start server:
make start
```

### Running locally

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
