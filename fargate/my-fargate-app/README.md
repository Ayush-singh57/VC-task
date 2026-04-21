# AWS Fargate Serverless Container Deployment

## Overview
This directory contains a containerized web application (`my-fargate-app`) configured for deployment on **AWS Fargate**, the serverless compute engine for Amazon Elastic Container Service (ECS). 

Instead of provisioning and managing EC2 instances, this project utilizes Fargate to abstract the underlying infrastructure, allowing the application to scale dynamically based on container metrics while maintaining high security and availability.

## 🏗️ Architecture Flow
1. **Containerization:** The application is packaged into a lightweight, isolated Docker container.
2. **Registry:** The Docker image is pushed to an **Amazon Elastic Container Registry (ECR)** repository.
3. **Task Definition:** An ECS Task Definition specifies the container image, required CPU/Memory, and port mappings.
4. **Fargate Service:** An ECS Service runs the Task on the Fargate serverless cluster, placing it behind an **Application Load Balancer (ALB)** for public access and traffic distribution.

## 🗂️ Project Structure

```text
📦 fargate/
 ┣ 📂 my-fargate-app/
 ┃ ┣ 📂 src/             # Source code (React/Node components)
 ┃ ┣ 📂 public/          # Static assets
 ┃ ┣ 📜 Dockerfile       # Instructions for building the container image
 ┃ ┣ 📜 package.json     # Application dependencies
 ┃ ┗ 📜 .dockerignore    # Files excluded from the build context