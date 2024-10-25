<div align="center">

# Jenkins CI/CD for ToDo List App

![Jenkins](https://github-repo-img.s3.eu-central-1.amazonaws.com/todo.png)

![Pipline](https://github-repo-img.s3.eu-central-1.amazonaws.com/todo-pip.png)

![Sonar](https://github-repo-img.s3.eu-central-1.amazonaws.com/todo-sonar.png)

![Argo](https://github-repo-img.s3.eu-central-1.amazonaws.com/todo-argo.png)

![Python Version](https://img.shields.io/badge/python-3.8%2B-blue) ![Deployment](https://img.shields.io/badge/k8s-deployed-success) ![ArgoCD](https://img.shields.io/badge/ArgoCD-synced-brightgreen) ![Docker Pulls](https://img.shields.io/docker/pulls/weronikastepien/cicd-todo)












------------


![Static Badge](https://img.shields.io/badge/Table%20%20%20%20%20%20%20%20%20%20%20of%20%20%20%20%20%20%20%20%20%20Contents-blue?style=for-the-badge&logoColor=darkviolet)

**| [Overview](#overview) | [Architecture](#architecture) | [Pipeline Breakdown](#pipeline-breakdown) |**





------------



## Overview
This CI/CD pipeline is designed for a Python Django To-Do List web application. It automates the entire software development lifecycle, from code integration, testing, and analysis to deployment on Kubernetes clusters using tools like Jenkins, Docker, and ArgoCD.




------------



</div>

## Architecture
The architecture of the CI/CD setup includes:

- Jenkins: Automates build, test, and deployment processes.
- Docker: Containerizes the application for consistent and reproducible environments.
- SonarQube: Performs static code analysis to maintain code quality.
- Kubernetes: Manages deployment, scaling, and management of containerized applications.
- ArgoCD: Handles application deployment and continuous delivery in Kubernetes.

The CI/CD pipeline integrates these tools to provide a seamless workflow for building, testing, and deploying the Django app.

------------
## Pipeline Breakdown
The CI/CD pipeline consists of the following stages:

#### I. Checkout

   - Clones the latest code from the GitHub repository.
   - Uses credentials (`github-id`) for secure access.
   - Fetches the code from the `main` branch.

#### II. Install SonarQube Scanner

  - Sets up the SonarQube scanner to perform static code analysis.
  - Installs required tools (`wget` and `unzip`) using `apt-get`.
  - Downloads the SonarQube scanner CLI and sets it up for use in subsequent stages.

#### III. Static Code Analysis

   - Analyzes the codebase for bugs, vulnerabilities, and code quality using SonarQube.
   - Authenticates with SonarQube using a token stored in Jenkins credentials (`sonarqube`).
   - Runs the scanner in the project directory (`CI_CD-Python-WebApp-ToDoList/ToDo`), scanning all source files.
   - Reports findings to SonarQube with the project key `CI_CD_Python_ToDoList`.

#### IV. Build and Push Docker Image

  - Builds the Docker image for the application and pushes it to DockerHub.
  - The image is tagged with the current `BUILD_NUMBER` for version tracking.
  - Uses Docker credentials (`docker-cred`) to push the image securely.

#### V. Update Kubernetes Manifest

  - Updates the Kubernetes deployment manifest to use the new Docker image version.
  - Uses the `sed` command to replace the image version in `minikube-todo-deploy.yaml`.
  - Commits and pushes the updated manifest back to the GitHub repository using stored credentials.

#### VI. Deploy to ArgoCD

  - Deploys the updated application to Kubernetes using ArgoCD.
  - Authenticates with ArgoCD using credentials (`argocd-cred`).
  - Uses the ArgoCD API to trigger a sync for the `todo` application, deploying the updated image and configuration.

Each of these stages ensures that the code is tested, analyzed for quality, containerized, and deployed efficiently, aligning with CI/CD practices.







