FROM python:3.12

WORKDIR /app

RUN pip install pytest
RUN pip install requests types-requests
RUN pip install flake8 black mypy

COPY tests /app/tests
COPY .flake8 /app
COPY mypy.ini /app
COPY pyproject.toml /app
COPY pytest.ini /app

RUN flake8 tests
RUN black --check --diff .
RUN mypy tests

RUN apt-get update && apt-get install -y curl

ENTRYPOINT ["python", "-m", "pytest", "-k", "tests", "-s"]
