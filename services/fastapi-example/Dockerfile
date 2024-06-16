FROM python:3.12


WORKDIR /app

RUN pip install fastapi uvicorn
COPY src /app/src

EXPOSE 8000

ENTRYPOINT ["uvicorn", "--host", "0.0.0.0", "--port", "8000", "src.app:app"]
