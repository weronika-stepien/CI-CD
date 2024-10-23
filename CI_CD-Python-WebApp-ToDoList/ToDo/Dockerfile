# Using an official Python runtime as a parent image
FROM python:3.12-slim

# Setting the working directory in the container
WORKDIR /app

# Copying the current directory contents into the container at /app
COPY . /app

# Installing any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Exposing the port the app runs on (adjust if your app runs on a different port)
EXPOSE 8000

# Defining environment variable to disable buffering
ENV PYTHONUNBUFFERED=1

# Running the application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

