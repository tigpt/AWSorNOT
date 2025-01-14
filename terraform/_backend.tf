terraform {
  backend "s3" {
    bucket         = "tf-awsornot-backend-3978-state"
    key            = "AWSorNOT.tfstate"
    region         = "eu-west-1"
    profile        = "tig-AWSorNOT"
    dynamodb_table = "tf-awsornot-backend-3978-locktable"
    encrypt        = true
  }
}
