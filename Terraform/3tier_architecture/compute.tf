data "aws_ami" "ubuntu" {
  most_recent = true
  owners      = ["099720109477"]
  filter {
    name   = "name"
    values = ["ubuntu/images/hvm-ssd/ubuntu-jammy-22.04-amd64-server-*"]
  }
}

# ==========================================
# TIER 3: THE DATABASE SERVER (MySQL)
# ==========================================
resource "aws_instance" "db_server" {
  ami                    = data.aws_ami.ubuntu.id
  instance_type          = "t3.micro"
  subnet_id              = aws_subnet.public_1.id 
  vpc_security_group_ids = [aws_security_group.db_sg.id]
  tags = { Name = "Tier-3-DB" }

  user_data = <<-EOF
              #!/bin/bash
              sleep 30
              sudo apt update
              sudo apt install mysql-server -y
              
              sudo sed -i 's/127.0.0.1/0.0.0.0/g' /etc/mysql/mysql.conf.d/mysqld.cnf
              sudo systemctl restart mysql
              
              sudo mysql -e "CREATE DATABASE virtuecloud;"
              sudo mysql -e "CREATE USER 'admin'@'%' IDENTIFIED BY 'password';"
              sudo mysql -e "GRANT ALL PRIVILEGES ON virtuecloud.* TO 'admin'@'%';"
              sudo mysql -e "FLUSH PRIVILEGES;"
              sudo mysql -e "USE virtuecloud; CREATE TABLE users (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(50), task VARCHAR(100));"
              sudo mysql -e "USE virtuecloud; INSERT INTO users (name, task) VALUES ('Ayush', 'Deployed a Full 3-Tier Architecture!');"
              EOF
}

# ==========================================
# TIER 2: THE APP SERVER (Node.js / Express)
# ==========================================
resource "aws_instance" "app_server" {
  ami                    = data.aws_ami.ubuntu.id
  instance_type          = "t3.micro"
  subnet_id              = aws_subnet.public_1.id 
  vpc_security_group_ids = [aws_security_group.app_sg.id]
  tags = { Name = "Tier-2-App" }

  user_data = <<-EOF
              #!/bin/bash
              sleep 120 
              curl -fsSL https://deb.nodesource.com/setup_20.x | sudo -E bash -
              sudo apt-get install -y nodejs
              
              mkdir /app && cd /app
              npm init -y
              npm install express mysql2 cors
              
              cat << 'EONODE' > server.js
              const express = require('express');
              const mysql = require('mysql2');
              const app = express();
              
              const db = mysql.createConnection({
                host: '${aws_instance.db_server.private_ip}',
                user: 'admin',
                password: 'password',
                database: 'virtuecloud'
              });
              
              app.get('/api/data', (req, res) => {
                db.query('SELECT * FROM users', (err, results) => {
                  if (err) res.status(500).send(err);
                  else res.json(results);
                });
              });
              
              app.listen(5000, '0.0.0.0', () => console.log('App running on port 5000'));
              EONODE
              
              nohup node server.js > app.log 2>&1 &
              EOF
}

# ==========================================
# TIER 1: THE WEB SERVER (Nginx)
# ==========================================
resource "aws_instance" "web_server" {
  ami                    = data.aws_ami.ubuntu.id
  instance_type          = "t3.micro"
  subnet_id              = aws_subnet.public_1.id
  vpc_security_group_ids = [aws_security_group.web_sg.id]
  tags = { Name = "Tier-1-Web" }

  # CRITICAL FIX: The Nginx config no longer contains backslashes that crash the server
  user_data = <<-EOF
              #!/bin/bash
              sleep 45 
              sudo apt update
              sudo apt install nginx -y

              cat << 'EOHTML' > /var/www/html/index.html
              <!DOCTYPE html>
              <html>
              <head>
                  <meta charset="UTF-8">
                  <title>3-Tier Dashboard</title>
                  <style>
                      body { font-family: Arial, sans-serif; text-align: center; margin-top: 100px; background-color: #f4f4f9; }
                      button { padding: 15px 30px; font-size: 18px; cursor: pointer; background-color: #007bff; color: white; border: none; border-radius: 5px; }
                      button:hover { background-color: #0056b3; }
                      #result { margin-top: 30px; font-size: 24px; color: #28a745; font-weight: bold; }
                      .error { color: #dc3545 !important; }
                  </style>
              </head>
              <body>
                  <h1>VirtueCloud Architecture Dashboard</h1>
                  <button onclick="fetchData()">Query Private Database</button>
                  <div id="result">Waiting for user action...</div>

                  <script>
                      function fetchData() {
                          let resDiv = document.getElementById('result');
                          resDiv.innerText = "Routing request through subnets...";
                          resDiv.classList.remove('error');
                          
                          fetch('/api/data')
                              .then(response => {
                                  if(!response.ok) throw new Error("Backend Offline");
                                  return response.json();
                              })
                              .then(data => {
                                  let user = data[0];
                                  resDiv.innerText = "✅ Success: " + user.name + " - " + user.task;
                              })
                              .catch(err => {
                                  resDiv.innerText = "❌ Connection Failed. The App Server is still booting up!";
                                  resDiv.classList.add('error');
                              });
                      }
                  </script>
              </body>
              </html>
              EOHTML

              cat << 'EONGINX' > /etc/nginx/sites-available/default
              server {
                  listen 80 default_server;
                  root /var/www/html;
                  index index.html;

                  location / {
                      try_files $uri $uri/ =404;
                  }

                  location /api/ {
                      proxy_pass http://${aws_instance.app_server.private_ip}:5000;
                      proxy_set_header Host $host;
                      proxy_set_header X-Real-IP $remote_addr;
                  }
              }
              EONGINX

              sudo systemctl restart nginx
              EOF
}

# ==========================================
# LOAD BALANCER & OUTPUTS
# ==========================================
resource "aws_lb" "main_alb" {
  name               = "virtuecloud-alb"
  internal           = false
  load_balancer_type = "application"
  security_groups    = [aws_security_group.alb_sg.id]
  subnets            = [aws_subnet.public_1.id, aws_subnet.public_2.id]
}

resource "aws_lb_target_group" "web_tg" {
  name     = "web-target-group"
  port     = 80
  protocol = "HTTP"
  vpc_id   = aws_vpc.main.id
}

resource "aws_lb_listener" "front_end" {
  load_balancer_arn = aws_lb.main_alb.arn
  port              = "80"
  protocol          = "HTTP"
  default_action {
    type             = "forward"
    target_group_arn = aws_lb_target_group.web_tg.arn
  }
}

resource "aws_lb_target_group_attachment" "web_attach" {
  target_group_arn = aws_lb_target_group.web_tg.arn
  target_id        = aws_instance.web_server.id
  port             = 80
}

output "live_website_url" {
  description = "Click this link to view your live architecture"
  value       = "http://${aws_lb.main_alb.dns_name}"
}