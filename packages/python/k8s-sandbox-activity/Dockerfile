FROM python:3.12

WORKDIR /app

RUN pip install flake8 black mypy

COPY src /app/src
COPY .flake8 /app
COPY mypy.ini /app
COPY pyproject.toml /app

RUN flake8 src
RUN black --check --diff .
RUN mypy src

ENTRYPOINT ["echo", "Linting passed"]
