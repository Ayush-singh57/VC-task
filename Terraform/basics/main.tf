provider "aws" {
  region = "ap-south-1"
}

 # Data Type 1: A List (An ordered collection of strings)
variable "new_hires" {
  type    = list(string)
  default = ["alice-dev", "bob-dev", "charlie-dev"]
}

# Data Type 2: A Map (Key-Value pairs, like a Python Dictionary)
variable "company_tags" {
  type = map(string)
  default = {
    Department = "Engineering"
    Project    = "MindfulMe"
    ManagedBy  = "Terraform"
  }
}

# --- 2. THE LOOP ---

resource "aws_iam_user" "employees" {
  # The Loop: "Count how many names are in the list, and run this block that many times"
  count = length(var.new_hires)
  
  # count.index is the current loop number (0, 1, 2)
  # It grabs "alice-dev" on loop 0, "bob-dev" on loop 1, etc.
  name = var.new_hires[count.index] 

  # We assign the map of tags to every single user automatically
  tags = var.company_tags
}

# --- 3. THE OUTPUT ---

output "created_users" {
  description = "The names of the users created by the loop"
  # The [*] tells Terraform to print the names of ALL users created by the loop
  value = aws_iam_user.employees[*].name 
}