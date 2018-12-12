# Use an official Python runtime as a parent image
FROM python:3.7-slim

ADD . /app

COPY . /app

WORKDIR /app

EXPOSE 5000

RUN pip install -r requirements.txt

CMD ["python", "app.py"]

