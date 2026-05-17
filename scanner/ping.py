import subprocess
import concurrent.futures

def ping_host(ip):
    result = subprocess.run(
        ["ping", "-c", "1", "-W", "1000", ip],
        capture_output=True
    )
    return ip if result.returncode == 0 else None

def ping_sweep(subnet_base, start=1, end=254):
    ips = [f"{subnet_base}.{i}" for i in range(start, end + 1)]
    with concurrent.futures.ThreadPoolExecutor(max_workers=100) as ex:
        results = list(ex.map(ping_host, ips))
    return [ip for ip in results if ip]