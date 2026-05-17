import socket
import subprocess
import time

def resolve_dns(hostname):
    try:
        return socket.gethostbyname(hostname)
    except socket.gaierror as e:
        return f"Error: {e}"

def reverse_dns(ip):
    try:
        return socket.gethostbyaddr(ip)[0]
    except socket.herror:
        return "No PTR record found"

def measure_rtt(host, port=80, timeout=2):
    start = time.time()
    try:
        with socket.create_connection((host, port), timeout):
            return round((time.time() - start) * 1000, 2)
    except:
        return None

def traceroute(host):
    result = subprocess.run(
        ["traceroute", "-m", "15", host],
        capture_output=True, text=True
    )
    return result.stdout