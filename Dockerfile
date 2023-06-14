ARG PYTHON_VERSION=3.10.11-slim-bullseye

FROM python:${PYTHON_VERSION} as python_stage

RUN apt-get update && \
    apt-get install -y git

RUN git clone https://github.com/dmitrylala/hse-algo
WORKDIR /hse-algo

# Install poetry
RUN python -m pip install --upgrade pip && pip install poetry -U

# Installing dependencies
RUN poetry config virtualenvs.create false \
    && poetry install
