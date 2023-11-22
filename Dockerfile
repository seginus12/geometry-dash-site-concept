FROM python:3.9.18-slim
RUN pip install --upgrade pip
RUN apt-get update
RUN apt-get install make
ENV PYTHONDONTWRITEBYTECODE=1 
ENV PYTHONUNBUFFERED=1
ENV DJANGO_SUPERUSER_PASSWORD=password 
WORKDIR /code 
COPY requirements.txt /code/ 
RUN pip install -r requirements.txt 
COPY . /code/