#!/usr/bin/env python
from getpass import getpass
from rich import print
from napalm import get_network_driver

cisco3 = {
    "hostname": "cisco3.lasthop.io",
    "username": "pyclass",
    "password": getpass(),
    "optional_args": {},
}

driver = get_network_driver("ios")
device = driver(**cisco3)

print()
print("\n\n>>>Test device open")
device.open()
output = device.get_facts()

print()
print(output)
print()
