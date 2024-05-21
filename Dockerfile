FROM python:latest
LABEL authors="picadio, refokcer"

WORKDIR app

COPY requirements.txt .
RUN ["pip3", "install", "-r", "./requirments.txt", "--no-cache-dir"]

COPY . .

RUN ["python3", "manage.py", "migrate"]

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
