FROM python:3.12

WORKDIR /app

RUN pip install poetry

RUN poetry config virtualenvs.create false

COPY pyproject.toml /app

RUN poetry install --no-root

COPY src /app/src
COPY .flake8 /app
COPY mypy.ini /app

RUN poetry install

RUN flake8 src
RUN black --check --diff .
RUN mypy src

EXPOSE 8000

ENTRYPOINT ["uvicorn", "--host", "0.0.0.0", "--port", "8000", "src.app:app"]
