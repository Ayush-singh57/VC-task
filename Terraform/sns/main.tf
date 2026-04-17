provider "aws" {
  region = "ap-south-1"
}

resource "aws_sns_topic" my_topic {
    name = "my-topic"
}

output "topic_arn" {
    value = aws_sns_topic.my_topic.arn
}