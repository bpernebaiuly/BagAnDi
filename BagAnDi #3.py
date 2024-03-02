import ipaddress

def validate_ip_address(ip_address):
    try:
        ip = ipaddress.ip_address(ip_address)
        return True, ip.version
    except ValueError:
        return False, None

def convert_ipv4_to_ipv6(ipv4_address):
    ipv6_address = ipaddress.IPv6Address('::ffff:' + ipv4_address)
    return str(ipv6_address)

def convert_ipv6_to_ipv4(ipv6_address):
    ipv4_address = ipaddress.IPv4Address(ipv6_address.replace('::ffff:', ''))
    return str(ipv4_address)

def calculate_subnet(ip_address, subnet_mask):
    network = ipaddress.ip_network(ip_address + '/' + subnet_mask, strict=False)
    return network.network_address, network.broadcast_address

# Пример использования функций

# Валидация IPv4 адреса
ip = "192.0.2.1"
valid, version = validate_ip_address(ip)
if valid:
    print(f"The IP address {ip} is valid IPv{version}.")
else:
    print(f"The IP address {ip} is invalid.")

# Конвертация IPv4 в IPv6
ipv4 = "192.0.2.1"
ipv6 = convert_ipv4_to_ipv6(ipv4)
print(f"IPv4 address {ipv4} converted to IPv6: {ipv6}")

# Конвертация IPv6 в IPv4
ipv6 = "2001:db8::1"
ipv4 = convert_ipv6_to_ipv4(ipv6)
print(f"IPv6 address {ipv6} converted to IPv4: {ipv4}")

# Расчет подсети
ip = "192.0.2.1"
subnet_mask = "255.255.255.0"
network_address, broadcast_address = calculate_subnet(ip, subnet_mask)
print(f"Network Address: {network_address}, Broadcast Address: {broadcast_address}")
