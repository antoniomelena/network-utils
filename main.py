import argparse
from scanner.ping import ping_sweep
from scanner.ports import scan_host
from scanner.diagnostics import resolve_dns, measure_rtt, traceroute
from utils.output import print_open, print_closed, print_info, print_warn

parser = argparse.ArgumentParser(prog="netutils")
sub = parser.add_subparsers(dest="command")

sweep_p = sub.add_parser("sweep", help="Find live hosts on a subnet")
sweep_p.add_argument("subnet", help="e.g. 192.168.1")

scan_p = sub.add_parser("scan", help="Scan open ports on a host")
scan_p.add_argument("host")

diag_p = sub.add_parser("diag", help="Run diagnostics on a hostname")
diag_p.add_argument("host")

args = parser.parse_args()

if args.command == "sweep":
    print_info(f"Sweeping {args.subnet}.1-254 ...")
    hosts = ping_sweep(args.subnet)
    for h in hosts:
        print_open(h)
    print_info(f"{len(hosts)} host(s) found")

elif args.command == "scan":
    print_info(f"Scanning {args.host} ...")
    results = scan_host(args.host)
    for r in sorted(results, key=lambda x: x["port"]):
        if r["open"]:
            msg = f"Port {r['port']} open"
            if r["banner"]:
                msg += f"  —  {r['banner'][:60]}"
            print_open(msg)

elif args.command == "diag":
    ip = resolve_dns(args.host)
    print_info(f"DNS: {args.host} -> {ip}")
    rtt = measure_rtt(args.host)
    if rtt:
        print_info(f"RTT to port 80: {rtt}ms")
    print_info("Traceroute:")
    print(traceroute(args.host))

else:
    parser.print_help()