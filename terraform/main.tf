provider "aws" {
  region = "eu-west-2"
}

resource "aws_instance" "devops_server" {
  ami           = "ami-0c76bd4bd302b30ec"
  instance_type = "t2.micro"

  tags = {
    Name = "DevOpsInstance"
  }
}

