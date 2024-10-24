# Using an official Python runtime as a parent image
FROM python:3.12-slim

# Setting the working directory in the container
WORKDIR /app

# Copying the current directory contents into the container at /app
COPY . /app

# Install dependencies and Docker CLI
RUN apt-get update && \
    apt-get install -y \
    apt-transport-https \
    ca-certificates \
    curl \
    gnupg2 \
    software-properties-common wget unzip && \
    curl -fsSL https://download.docker.com/linux/debian/gpg | apt-key add - && \
    add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/debian $(lsb_release -cs) stable" && \
    apt-get update && \
    apt-get install -y docker-ce-cli && \
    # Install SonarQube scanner
    wget -qO- https://binaries.sonarsource.com/Distribution/sonar-scanner-cli/sonar-scanner-cli-4.7.0.2747-linux.zip -O /tmp/sonar-scanner.zip && \
    unzip /tmp/sonar-scanner.zip -d /opt && \
    ln -s /opt/sonar-scanner-4.7.0.2747-linux/bin/sonar-scanner /usr/local/bin/sonar-scanner && \
    # Clean up
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Exposing the port the app runs on (adjust if your app runs on a different port)
EXPOSE 8000

# Defining environment variable to disable buffering
ENV PYTHONUNBUFFERED=1

# Set Docker environment variable to connect to the host Docker daemon
ENV DOCKER_HOST=unix:///var/run/docker.sock

# Running the application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
