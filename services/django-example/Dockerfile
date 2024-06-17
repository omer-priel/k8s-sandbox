FROM python:3.12

WORKDIR /app

RUN pip install Django

COPY . ./

EXPOSE 8000

ENTRYPOINT ["python", "manage.py", "runserver", "0.0.0.0:8000"]
