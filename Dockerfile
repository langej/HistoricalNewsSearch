# Use an official Python runtime as a parent image
FROM python:3.7-slim

ADD . /code

# Set the working directory to /app
WORKDIR /code

# Copy the current directory contents into the container at /app
COPY . /app

# Define environment variable
# ENV NAME World

RUN pip install -r requirements.txt
# Run main.py when the container launches
CMD ["python", "app.py"]
