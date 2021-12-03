#!/usr/bin/env python
"""Exercises using Netmiko"""
from __future__ import print_function
from getpass import getpass
from netmiko import ConnectHandler


def main():
    """Exercises using Netmiko"""
    passwd = getpass("Enter password: ")

    device = {
        "device_type": "cisco_nxos",
        "host": "nxos1.lasthop.io",
        "username": "pyclass",
        "password": passwd,
    }

    cfg_commands = [
        "ntp server 130.126.24.24 use-vrf management",
        "ntp server 152.2.21.1 use-vrf management",
    ]

    for a_device in [device]:
        with ConnectHandler(**a_device) as net_connect:
            print("Current Prompt: " + net_connect.find_prompt())
            output = net_connect.send_config_set(cfg_commands)
            save_output = net_connect.save_config()

        print("\nConfiguring...")
        print("#" * 80)
        print("\nSaving config to startup")
        print(output)
        print(save_output)
        print("#" * 80)
        print()


if __name__ == "__main__":
    main()
