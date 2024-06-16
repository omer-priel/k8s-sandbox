FROM python:3.12


WORKDIR /app

RUN pip install flask gunicorn
COPY src /app/src

EXPOSE 8000

ENTRYPOINT ["gunicorn", "-b", "0.0.0.0", "src.app:app"]
