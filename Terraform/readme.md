# AWS Infrastructure as Code (IaC) using Terraform 🏗️☁️

## Overview
This directory contains a collection of Terraform configurations used to provision, manage, and destroy AWS cloud infrastructure automatically. By treating infrastructure as code, these projects eliminate manual console configurations, ensuring that all environments are reproducible, version-controlled, and highly scalable.

The projects range from fundamental Terraform concepts (variable manipulation, data types) to complex, production-ready networking and compute architectures.

## 🗂️ Project Structure

The repository is divided into specific modules and projects:

```text
📦 Terraform/
 ┣ 📂 3tier_architecture/  # A complete, highly available web/app/db stack
 ┣ 📂 basics/              # Core IaC concepts: Variables (Lists, Maps), Loops
 ┣ 📂 s3/                  # Automated provisioning of secure object storage
 ┗ 📂 sns/                 # Simple Notification Service topic configurations