#!/usr/bin/env python
from getpass import getpass
from netmiko import ConnectHandler

password = getpass()

arista1 = {
    "device_type": "arista_eos",
    "host": "arista1.lasthop.io",
    "username": "pyclass",
    "password": password,
}

arista2 = {
    "device_type": "arista_eos",
    "host": "arista2.lasthop.io",
    "username": "pyclass",
    "password": password,
}

arista3 = {
    "device_type": "arista_eos",
    "host": "arista3.lasthop.io",
    "username": "pyclass",
    "password": password,
}

arista4 = {
    "device_type": "arista_eos",
    "host": "arista4.lasthop.io",
    "username": "pyclass",
    "password": password,
}

for device in (arista1, arista2, arista3, arista4):
    net_connect = ConnectHandler(**device)
    output = net_connect.send_command("show ip int brief")

    print()
    print(f"Host: {net_connect.host}:{net_connect.port}")
    print("-" * 50)
    print(output)
    print("-" * 50)
    net_connect.disconnect()
