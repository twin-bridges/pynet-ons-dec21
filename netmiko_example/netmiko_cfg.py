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

cfg_commands = [
    "ntp server 130.126.24.24",
    "ntp server 152.2.21.1",
]

with ConnectHandler(**device) as net_connect:
    # output = net_connect.send_config_set(cfg_commands, error_pattern=r"% Invalid")
    output = net_connect.send_config_set(cfg_commands)
    output += net_connect.save_config()

print("-" * 50)
print(output)
print("-" * 50)
