# Network Utils

A command-line Python tool for local network scanning and diagnostics.
Built using Python socket programming.

## Install
```
git clone https://github.com/YOUR_USERNAME/network-utils.git
cd network-utils
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Usage
```
python main.py sweep 192.168.1       # find live hosts
python main.py scan 192.168.1.1      # scan open ports
python main.py diag google.com       # DNS + speed + traceroute
```