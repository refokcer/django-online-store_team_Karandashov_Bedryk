FROM python:latest
LABEL authors="picadio, refokcer"

ENV PYTHONUNBUFFERED=1

WORKDIR app

COPY requirements.txt .
RUN ["pip3", "install", "-r", "./requirements.txt", "--no-cache-dir"]

COPY . .


