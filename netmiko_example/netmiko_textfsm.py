#!/usr/bin/env python
from getpass import getpass
from rich import print
from netmiko import ConnectHandler

if __name__ == "__main__":

    password = getpass("Enter password: ")
    device = {
        "device_type": "juniper_junos",
        "host": "vmx1.lasthop.io",
        "username": "pyclass",
        "password": password,
        "session_log": "my_session.txt",
    }

    net_connect = ConnectHandler(**device)
    print(net_connect.send_command("show interfaces", use_textfsm=True))
    net_connect.disconnect()
