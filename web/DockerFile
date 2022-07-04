FROM python:3

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /code/web
COPY requirements.txt /code/web
RUN pip install -r requirements.txt
COPY . /code/web
