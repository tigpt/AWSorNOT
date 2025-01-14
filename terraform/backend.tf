module "remote-state-s3-dynamodb-backend" {
  source  = "tigpt/remote-state-s3-dynamodb-backend/aws"
  version = "1.0.2"

  name = "awsornot-backend"
}
