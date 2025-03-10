import subprocess
import ipaddress

__author__ = "Benedikt theuretzbachner"


ip = input("[ipaddress/cidr]> ")
try:
    ip = ipaddress.ip_network(ip)
except Exception:
    raise Exception("ip address invalid")

for addr in ip.hosts():
    subprocess.run(["ping", "-c4", str(addr)])
