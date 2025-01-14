provider "aws" {
  profile = "tig-AWSorNOT"
  region  = "eu-west-1"
  default_tags {
    tags = {
      terraform  = "true"
      repository = "http://github.com/tigpt/AWSorNOT"
    }
  }

}
