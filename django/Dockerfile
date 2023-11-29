FROM python:3.9.18-slim
ENV PYTHONDONTWRITEBYTECODE=1 
ENV PYTHONUNBUFFERED=1
ENV DJANGO_SUPERUSER_PASSWORD=password 
WORKDIR /usr/src/app

RUN apt-get update && \
    apt-get install make

COPY requirements.txt /usr/src/app

RUN pip install --upgrade pip && \
    pip install -r requirements.txt 

COPY . /usr/src/app