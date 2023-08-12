import socket

def dns_lookup(domain_name):
    try:
        ip_address = socket.gethostbyname(domain_name)
        print(f"The IP address of {domain_name} is {ip_address}")
    except socket.gaierror:
        print(f"DNS lookup failed for {domain_name}")

# Replace "example.com" with the domain name you want to look up
domain_to_lookup = "intec.edu.do"
dns_lookup(domain_to_lookup)