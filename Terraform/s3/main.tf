provider "aws" {
  region = "ap-south-1"
}

resource "aws_s3_bucket" "my_bucket" {
  bucket = "tf-bucket-2026-vc"
}

resource "aws_s3_object" "my_file" {
  bucket = aws_s3_bucket.my_bucket.id
  key = "cloud.secret.txt"
  source = "secret.txt"
}

# output 
output "bucket_name" {
  value = aws_s3_bucket.my_bucket.id
}