# devdiscover
A simple utility that can discover all LAN/WLAN devices in specified IP range

# Usage
./devdiscover.py --ip-start=[first_ip] --ip-end=[second_ip] [--show-macs] [--show-names] [--verbose] --wait-response=[seconds] --iface=[interface]

# Samples of using
<ul>
  <li>./devdiscover.py --ip-start=192.168.1.1 --ip-end=192.168.1.255 --show-names --wait-response=0.3 --iface=wlan0</li>
  <li>./devdiscover.py --ip-start=10.0.0.1 --ip-end=10.0.0.255 --show-macs --show-names --wait-response=0.2 --verbose --iface=eth0</li>
  
</ul>

# Installation
python3, dnsutils
