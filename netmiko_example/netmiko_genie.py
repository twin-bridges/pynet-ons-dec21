#!/usr/bin/env python
from getpass import getpass
import rich
from netmiko import ConnectHandler

if __name__ == "__main__":

    password = getpass("Enter password: ")
    device = {
        "device_type": "cisco_xe",
        "host": "cisco3.lasthop.io",
        "username": "pyclass",
        "password": password,
    }

    net_connect = ConnectHandler(**device)
    rich.print(net_connect.send_command("show ip int brief", use_genie=True))
    net_connect.disconnect()
