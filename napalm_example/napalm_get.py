#!/usr/bin/env python
from getpass import getpass
from rich import print
from napalm import get_network_driver

device = {
    "hostname": "arista4.lasthop.io",
    "username": "pyclass",
    "password": getpass(),
    "optional_args": {},
}

driver = get_network_driver("eos")
device = driver(**device)

print()
print("\n\n>>>Test device open")
device.open()
# output = device.get_lldp_neighbors()
# output = device.get_arp_table()
# output = device.get_interfaces_ip()
output = device.get_vlans()

print()
print(output)
print()
