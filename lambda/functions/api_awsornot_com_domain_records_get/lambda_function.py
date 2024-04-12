import json
import dns.resolver

def lambda_handler(event, context):
    # Check if 'queryStringParameters' exists and contains 'domain'
    domain_name = event.get('queryStringParameters', {}).get('domain')
    
    if not domain_name:
        return {
            'statusCode': 400,
            'body': json.dumps({'message': 'Missing domain query parameter'})
        }
    
    dns_records = {}
    record_types = ['A', 'AAAA', 'MX', 'NS', 'TXT', 'CNAME', 'SRV']
    
    for record_type in record_types:
        try:
            answers = dns.resolver.resolve(domain_name, record_type)
            dns_records[record_type] = [answer.to_text() for answer in answers]
        except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN, dns.resolver.NoNameservers):
            dns_records[record_type] = []

    return {
        'statusCode': 200,
        'body': json.dumps({
            'message': f'DNS lookup result for {domain_name}',
            'records': dns_records
        })
    }
