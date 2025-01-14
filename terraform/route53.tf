resource "aws_route53_zone" "primary" {
  name          = "awsornot.com"
  force_destroy = true
}

resource "aws_route53_record" "a" {
  name    = "awsornot.com"
  zone_id = aws_route53_zone.primary.zone_id
  type    = "A"

  alias {
    name                   = "deuk43gf4dzuz.cloudfront.net."
    zone_id                = "Z2FDTNDATAQYW2"
    evaluate_target_health = false
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
  name    = "api.awsornot.com"
  zone_id = aws_route53_zone.primary.zone_id
  type    = "A"

  alias {
    name                   = "d2a2q2tsjxjf6l.cloudfront.net."
    zone_id                = "Z2FDTNDATAQYW2"
    evaluate_target_health = false
  }
}
