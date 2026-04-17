data "aws_ami" "ubuntu" {
  most_recent = true
  owners      = ["099720109477"] 
  filter {
    name   = "name"
    values = ["ubuntu/images/hvm-ssd/ubuntu-jammy-22.04-amd64-server-*"]
  }
}

resource "aws_instance" "web_server" {
  ami                    = data.aws_ami.ubuntu.id
  instance_type          = "t3.micro"
  subnet_id              = aws_subnet.web_public.id
  vpc_security_group_ids = [aws_security_group.web_sg.id]
  key_name               = "wellness-key"
  tags = { Name = "TF-Web-Server" }
}

resource "aws_instance" "app_server" {
  ami                    = data.aws_ami.ubuntu.id
  instance_type          = "t3.micro"
  subnet_id              = aws_subnet.app_private.id
  vpc_security_group_ids = [aws_security_group.app_sg.id]
  key_name               = "wellness-key"
  tags = { Name = "TF-App-Server" }
}

resource "aws_instance" "db_server" {
  ami                    = data.aws_ami.ubuntu.id
  instance_type          = "t3.micro"
  subnet_id              = aws_subnet.db_private.id
  vpc_security_group_ids = [aws_security_group.db_sg.id]
  key_name               = "wellness-key"
  tags = { Name = "TF-DB-Server" }
}

output "web_public_ip" {
  value = aws_instance.web_server.public_ip
}
output "app_private_ip" {
  value = aws_instance.app_server.private_ip
}
output "db_private_ip" {
  value = aws_instance.db_server.private_ip
}