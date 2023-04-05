import socket

def get_domain_name(ip_address):
    return list(socket.gethostbyaddr((ip_address)))[0]

print(get_domain_name(input()))