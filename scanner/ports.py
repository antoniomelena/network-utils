import socket
import concurrent.futures

COMMON_PORTS = [21,22,23,25,53,80,110,143,443,3306,5432,8080]

def scan_port(host, port, timeout=1):
    try:
        with socket.create_connection((host, port), timeout) as s:
            try:
                banner = s.recv(1024).decode().strip()
            except:
                banner = ""
            return {"port": port, "open": True, "banner": banner}
    except:
        return {"port": port, "open": False, "banner": ""}

def scan_host(host, ports=None):
    ports = ports or COMMON_PORTS
    with concurrent.futures.ThreadPoolExecutor(max_workers=50) as ex:
        futures = [ex.submit(scan_port, host, p) for p in ports]
        return [f.result() for f in concurrent.futures.as_completed(futures)]
