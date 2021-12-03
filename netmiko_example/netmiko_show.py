#!/usr/bin/env python
from getpass import getpass
from netmiko import ConnectHandler

password = getpass()

device = {
    "device_type": "arista_eos",
    "host": "arista1.lasthop.io",
    "username": "pyclass",
    "password": password,
}

net_connect = ConnectHandler(**device)
output = net_connect.send_command("show lldp neighbors")
net_connect.disconnect()

print("-" * 50)
print(output)
print("-" * 50)
