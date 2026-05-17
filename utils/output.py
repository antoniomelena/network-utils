from colorama import Fore, Style, init
init(autoreset=True)

def print_open(msg):
    print(Fore.GREEN + "  [+] " + msg)

def print_closed(msg):
    print(Fore.RED + "  [-] " + msg)

def print_info(msg):
    print(Fore.CYAN + "  [*] " + msg)

def print_warn(msg):
    print(Fore.YELLOW + "  [!] " + msg)