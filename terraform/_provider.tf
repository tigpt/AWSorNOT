provider "aws" {
  region  = "eu-west-1"
  profile = "tig-AWSorNOT"
  default_tags {
    tags = {
      terraform = "true"
      repo      = "https://github.com/tigpt/AWSorNOT"
    }
  }
}
