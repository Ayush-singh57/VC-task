# AWS Cloud Automation with Python (Boto3) ☁️🐍

## Overview
This repository contains a suite of Python scripts utilizing the **AWS SDK for Python (Boto3)** to automate the provisioning, management, and monitoring of cloud infrastructure. These scripts were developed to replace manual AWS Console operations with programmatic, repeatable, and scalable DevOps practices.

By leveraging Boto3, this project demonstrates automated control over core AWS services including Compute (EC2), Storage (S3), Databases (DynamoDB), Security (IAM), and Monitoring (CloudWatch).

## 🗂️ Project Structure

The repository is modularized by AWS service for easy navigation and execution:

```text
📦 boto3/
 ┣ 📂 cloudwatch/
 ┃ ┗ 📜 create.py               # Configures CloudWatch metrics and alerts
 ┣ 📂 dynamodb/
 ┃ ┣ 📜 createTable.py          # Provisions NoSQL database tables
 ┃ ┣ 📜 putItem.py              # Inserts records into DynamoDB
 ┃ ┣ 📜 getItem.py              # Queries records
 ┃ ┣ 📜 updateT.py              # Updates table configurations/items
 ┃ ┣ 📜 deleteItem.py           # Removes specific records
 ┃ ┗ 📜 deleteTable.py          # Tears down DynamoDB tables
 ┣ 📂 ec2/
 ┃ ┣ 📜 launchI.py              # Provisions and launches new EC2 instances
 ┃ ┣ 📜 listInstances.py        # Retrieves state and metadata of active instances
 ┃ ┣ 📜 start.py                # Boots up stopped instances
 ┃ ┣ 📜 stopI.py                # Safely halts running instances to save costs
 ┃ ┗ 📜 terminate.py            # Permanently destroys EC2 instances
 ┣ 📂 IAM/
 ┃ ┗ 📜 create_role.py          # Generates secure IAM roles and policies
 ┣ 📂 s3/
 ┃ ┗ 📜 create_bucket.py        # Provisions secure object storage buckets
 ┗ 📂 serverless/
   ┗ 📜 (Lambda functions & triggers)