# devdiscover
A simple utility that can discover all LAN/WLAN devices in specified IP range

# Usage
./devdiscover.py --ip-start=[first_ip] --ip-end=[second_ip] [--show-macs] [--show-names] [--verbose] --wait-response=[seconds] --iface=[interface]

<table>
  <tr><th>Argument name</th><th>Description</th><th>Is necessary?</th></tr>
  <tr><td>--ip-start=[ip]</td><td>Start bound of IP range</td><td>*</td></tr>
  <tr><td>--ip-end=[ip]</td><td>End bound of IP range</td><td>*</td></tr>
  <tr><td>--show-macs</td><td>Show MAC addresses?</td><td></td></tr>
  <tr><td>--show-names</td><td>Show names of devices?</td><td></td></tr>
  <tr><td>--verbose</td><td>Show all scanned IP addresses</td><td></td></tr>
  <tr><td>--wait-response=[seconds]</td><td>How much time should I wait for response?</td><td>*</td></tr>
  <tr><td>--iface=[interface]</td><td>Which interface should I use to scan IP addresses?</td><td>*</td></tr>
</table>

# Samples of using (instead of ./devdiscover.py you can type devdiscover if copied the file to /usr/bin/devdiscover)
<ul>
  <li>./devdiscover.py --ip-start=192.168.1.1 --ip-end=192.168.1.255 --show-names --wait-response=0.3 --iface=wlan0</li>
  <li>./devdiscover.py --ip-start=10.0.0.1 --ip-end=10.0.0.255 --show-macs --show-names --wait-response=0.2 --verbose --iface=eth0</li>
  <li>./devdiscover.py --ip-start=192.168.0.23 --ip-end=192.168.0.106 --show-macs --verbose --wait-response=0.5 --iface=wlan1</li>
</ul>

# Installation
1. Install these packages using your package manager:<br>
   <i>python3, dnsutils, samba, net-tools, git</i>
2. Clone this repository:<br>
   <i>git clone https://github.com/thm-unix/devdiscover/</i>
3. <i>cd devdiscover</i>
4. Make 'devdiscover.py' executable:<br>
   <i>chmod +x ./devdiscover.py</i><br>
   
<i>(optional)</i>: if you want to, you can copy this file to /usr/bin/devdiscover and run it from anywhere just by typing devdiscover:<br>
   <i>sudo cp devdiscover.py /usr/bin/devdiscover</i>
