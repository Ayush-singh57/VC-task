#  Learning task 

> A comprehensive monorepo containing infrastructure-as-code, automation scripts, containerized applications, and CI/CD pipelines.

![AWS](https://img.shields.io/badge/AWS-%23FF9900.svg?style=for-the-badge&logo=amazon-aws&logoColor=white)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)
![Terraform](https://img.shields.io/badge/terraform-%235835CC.svg?style=for-the-badge&logo=terraform&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/github%20actions-%232671E5.svg?style=for-the-badge&logo=githubactions&logoColor=white)

## 📌 Overview
This repository serves as a centralized portfolio of the 23-task cloud engineering curriculum. It demonstrates hands-on proficiency in provisioning highly available architectures, writing automated deployment scripts, building modular CI/CD pipelines, and troubleshooting complex cloud networking issues.

---

## 📁 Repository Navigation

The projects are organized categorically. *Click into any folder to view the specific code, deployment scripts, and detailed documentation for that task.*

| Directory | Core Focus | Related Tasks |
| :--- | :--- | :--- |
| 🐍 `/botto3` | **Python Automation:** Scripts for managing EC2 lifecycles, S3 buckets, IAM user generation, and secure Presigned URLs. | Tasks 18, 19, 20, 21 |
| ⚙️ `/composite` | **CI/CD Abstraction:** Modular GitHub Actions composite workflows for reusable deployment logic. | Tasks 6, 7, 9 |
| 🚀 `/deveops_prac` | **DevOps Workflows:** Standardized GitHub Actions pipelines for React and Spring Boot. | Tasks 5, 9 |
| 🐳 `/Docker_stuffs` | **Containerization:** Dockerfiles and containerization strategies for Python Flask apps. | Tasks 15, 16 |
| 🖥️ `/ECS_EC@` | **Container Orchestration (EC2):** Deploying ECS clusters backed by self-managed EC2 capacity and ALBs. | Task 23 |
| ☁️ `/fargate` | **Serverless Compute:** Abstracting infrastructure using AWS Fargate for zero-maintenance container deployments. | Task 10 |
| 🐘 `/LAMP` | **Stack Deployment:** Docker-compose implementations for full LAMP and Maven/Spring Boot stacks. | Task 17 |
| 🪣 `/s3_l` | **Cloud Storage:** Static website hosting, cross-region replication, and S3-to-SNS event notifications. | Tasks 2, 3, 4 |
| ☕ `/springboot` | **Backend Deployment:** End-to-end Maven & Spring Boot application deployments on AWS EC2. | Task 8 |
| 🏗️ `/Terraform` | **Infrastructure as Code (IaC):** Provisioning complete 3-Tier architectures (VPC, EC2, RDS) using Terraform. | Tasks 11, 12 |

---

1. **The EC2 to Fargate Pivot:** Diagnosed a persistent `Container instances (0)` cluster registration error by analyzing underlying Linux agent logs. Resolved the IAM race condition and architectural bottleneck by migrating the workload to a serverless AWS Fargate model.
2. **CI/CD Pipeline Modularity:** Overcame "Runner Amnesia" in GitHub Actions by restructuring checkout sequences, allowing for highly modular, reusable composite actions that streamlined frontend deployments.
3. **Automated Cost Optimization:** Authored Python Boto3 scripts to automatically scan AWS accounts and shut down idle developer EC2 environments, applying strict FinOps principles.
4. **Persistent EC2 Reverse Proxies:** Deployed raw Flask web servers on EC2, utilizing Linux `nohup` for background persistence and configuring Nginx as a reverse proxy to securely route traffic from Port 80 to Port 5000.

---

## 🛠️ Technology Stack Highlights
* **Cloud Provider:** Amazon Web Services (VPC, EC2, S3, ECS, Fargate, ALB, CloudWatch, SNS, IAM, RDS)
* **Automation & IaC:** Python (Boto3 SDK), HashiCorp Terraform
* **CI/CD:** GitHub Actions, Docker, Docker Compose
* **Web Servers & Networking:** Nginx, Linux (Ubuntu/Amazon Linux), SSH, Reverse Proxying

---

## 👨‍💻 Author
**Ayush Chouhan** *Cloud Engineering Intern*
> *"Building scalable, highly-available, and automated infrastructure from the ground up."*