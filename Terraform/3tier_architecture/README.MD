# 🏛️ 3-Tier AWS Architecture (Terraform)

## 📌 Objective
This module provisions a highly available, secure 3-Tier Architecture in AWS using Terraform. It automatically deploys the networking infrastructure, security groups, and compute resources required to host a decoupled full-stack application.

## 🏗️ Architecture Components
* **Public Tier:** Application Load Balancer (ALB) and Nginx Reverse Proxy.
* **App Tier (Private):** Node.js REST API running on EC2.
* **Database Tier (Private):** MySQL database running on EC2.

## ⚙️ How It Works
1. **`network.tf`**: Creates a custom VPC (`10.0.0.0/16`), an Internet Gateway, two Public Subnets, and two Private Subnets.
2. **`security.tf`**: Implements a Zero-Trust firewall. The Database only accepts Port 3306 traffic from the App Server. The App Server only accepts Port 5000 traffic from the Web Server. 
3. **`compute.tf`**: Utilizes `user_data` scripts to automatically install Nginx, Node.js, and MySQL on boot.

## 🚀 Execution
```bash
terraform init
terraform plan
terraform apply -auto-approve