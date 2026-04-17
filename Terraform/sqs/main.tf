provider "aws" {
  region = "ap-south-1"
}

resource "aws_sqs_queue" "my_queue" {
    name = "my-queue"
}

output "queue_url" {
    value = aws_sqs_queue.my_queue.id
}