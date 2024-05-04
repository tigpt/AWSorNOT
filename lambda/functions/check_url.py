from aws_xray_sdk.core import xray_recorder
import socket
import requests
import ipaddress
import json
from urllib.parse import urlparse

@xray_recorder.capture('extract_domain')
def extract_domain(url):
    # Parse the URL to extract components
    parsed_url = urlparse(url)
    # Return the network location part (domain)
    return parsed_url.netloc

@xray_recorder.capture('fetch_aws_ip_ranges')
def fetch_aws_ip_ranges():
    # URL for AWS IP ranges JSON
    url = "https://ip-ranges.amazonaws.com/ip-ranges.json"
    response = requests.get(url)
    aws_data = response.json()
    return aws_data['prefixes']

# Load AWS IP ranges
aws_prefixes = fetch_aws_ip_ranges()

@xray_recorder.capture('is_aws_hosted')
def is_aws_hosted(url):
    try:
        # Resolve IP address of the URL
        ip_address = socket.gethostbyname(url)
    except socket.gaierror:
        return False, "DNS resolution failed"

    # Check if IP in AWS ranges
    for prefix in aws_prefixes:
        network = ipaddress.ip_network(prefix['ip_prefix'])
        if ipaddress.ip_address(ip_address) in network:
            return True, f"Hosted on AWS ({prefix['service']})"
    return False, "Not hosted on AWS"

@xray_recorder.capture('handler')
def lambda_handler(event, context):
    # event contains the input data from Step Functions
    url = event['url']  # Extracting the URL passed from Step Functions
    domain = extract_domain(url)
    hosted, message = is_aws_hosted(domain)

    return {
        'url': url,
        'domain': domain,
        'aws_hosted': hosted,
        'message': message
    }
