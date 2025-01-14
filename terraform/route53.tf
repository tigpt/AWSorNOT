resource "aws_route53_zone" "primary" {
  name          = "awsornot.com"
  force_destroy = true
}

resource "aws_route53_record" "a" {
  zone_id = aws_route53_zone.primary.zone_id
  name    = "awsornot.com"
  type    = "A"

  alias {
    evaluate_target_health = false
    name                   = "deuk43gf4dzuz.cloudfront.net"
    zone_id                = "Z2FDTNDATAQYW2"
  }
}

resource "aws_route53_record" "cname" {
  zone_id = aws_route53_zone.primary.zone_id
  name    = "_1f2335fb9bd2b635e22581020e769652.awsornot.com"
  type    = "CNAME"
  ttl     = 300
  records = ["_e2710d63a527c59d75e135d8610cfdda.mhbtsbpdnt.acm-validations.aws."]
}


resource "aws_route53_record" "api" {
  zone_id = aws_route53_zone.primary.zone_id
  name    = "api.awsornot.com"
  type    = "A"

  alias {
    evaluate_target_health = false
    name                   = "d2a2q2tsjxjf6l.cloudfront.net."
    zone_id                = "Z2FDTNDATAQYW2"
  }
}
