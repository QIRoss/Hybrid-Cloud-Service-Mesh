provider "aws" {
  profile = "qiross"
  region  = "us-east-1"
}

resource "aws_instance" "my_ec2_instance" {
  ami                         = "ami-0866a3c8686eaeeba"
  instance_type               = "t2.micro"
  key_name                    = "qiross"
  subnet_id                   = "subnet-01fb57be965f0ab32"
  vpc_security_group_ids      = ["sg-06b1d2e2e843529f4","sg-09f4c9fee2f7789e8"]
  associate_public_ip_address = true

  tags = {
    Name = "Hybrid-Cloud-Service-Mesh-Instance"
  }

  provisioner "file" {
    source      = "./cloud-service"
    destination = "/home/ubuntu/cloud-service"
    connection {
      type        = "ssh"
      user        = "ubuntu"
      private_key = file("/home/qiross/.ssh/qiross.pem")
      host        = self.public_ip
    }
  }

  provisioner "remote-exec" {
    inline = [
      "sudo apt-get update -y",
      "sudo apt-get install -y docker.io docker-compose",
      "sudo systemctl start docker",
      "sudo systemctl enable docker",
      "sudo usermod -aG docker ubuntu",
      "cd /home/ubuntu/cloud-service",
      "sudo docker-compose up --build -d"
    ]
    connection {
      type        = "ssh"
      user        = "ubuntu"
      private_key = file("/home/qiross/.ssh/qiross.pem")
      host        = self.public_ip
    }
  }
}
