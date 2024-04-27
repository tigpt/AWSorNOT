import socket
import requests
import ipaddress
import json

def fetch_aws_ip_ranges():
    url = "https://ip-ranges.amazonaws.com/ip-ranges.json"
    response = requests.get(url)
    aws_data = response.json()
    return aws_data['prefixes']

def is_aws_hosted(url):
    try:
        # Resolve IP address of the URL
        ip_address = socket.gethostbyname(url)
    except socket.gaierror:
        return False, "DNS resolution failed"
    # Load AWS IP ranges
    aws_prefixes = fetch_aws_ip_ranges()
    # Check if IP in AWS ranges
    for prefix in aws_prefixes:
        network = ipaddress.ip_network(prefix['ip_prefix'])
        if ipaddress.ip_address(ip_address) in network:
            return True, f"Hosted on AWS ({prefix['service']})"
    return False, "Not hosted on AWS"

# Example usage
url = "awsornot.com"
hosted, message = is_aws_hosted(url)
print(f"{url} {message}")
