# Using an official Python runtime as the parent image
FROM python:3.11-slim

# Setting the working directory in the container
WORKDIR /app

# Copying the current directory contents into the container at /app
COPY . /app

# Installing any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Making port 5000 available to the world outside this container
EXPOSE 5000

# Defining environment variable for Flask
ENV FLASK_APP=main.py
ENV FLASK_ENV=development

# Running main.py when the container launches
CMD ["python", "main.py"]

