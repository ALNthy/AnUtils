import socket
from socket import AddressFamily


def get_network() -> dict[str, list]:
    hostname = socket.gethostname()
    addrs = socket.getaddrinfo(hostname, None)

    network_ipv4 = [item[4][0] for item in addrs if item[0] == AddressFamily.AF_INET]
    network_ipv6 = [item[4][0] for item in addrs if item[0] == AddressFamily.AF_INET6 and item[4][3] == 0]
    return {"ipv4": network_ipv4,
            "ipv6": network_ipv6}
