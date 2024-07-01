import socket


def get_ip_address(url):
    try:
        ipAddress = socket.gethostbyname(url)
        return ipAddress
    except socket.gaierror:
        return "Invalid URL or unable to resolve IP address."


if __name__ == "__main__":
    url = input("Enter the website URL (without 'http:// or 'https://'): ")
    ip_address = get_ip_address(url)
    print(f"The IP address of {url} is: {ip_address}")
