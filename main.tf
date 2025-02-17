terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
    }
  }
}


#1.create vpc

resource "aws_vpc" "main" {
  cidr_block       = "20.0.0.0/16"
  instance_tenancy = "default"

  tags = {
    Name = "production-vpc"
  }
}