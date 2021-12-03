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
print(net_connect.find_prompt())
net_connect.disconnect()
