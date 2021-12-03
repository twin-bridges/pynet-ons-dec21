#!/usr/bin/env python
"""Exercises using Netmiko"""
import os
from getpass import getpass
from netmiko import ConnectHandler


def save_file(filename, show_run):
    """Save the show run to a file"""
    with open(filename, "w") as f:
        f.write(show_run)


def main():
    """Exercises using Netmiko"""

    # For automated testing
    std_password = os.getenv("NETMIKO_PASSWORD")
    if std_password is None:
        std_password = getpass("Enter networking password: ")

    arista1 = {
        "device_type": "arista_eos",
        "host": "arista1.lasthop.io",
        "username": "pyclass",
        "password": std_password,
    }

    vmx1 = {
        "device_type": "juniper_junos",
        "host": "vmx1.lasthop.io",
        "username": "pyclass",
        "password": std_password,
    }

    for a_device in (arista1, vmx1):
        net_connect = ConnectHandler(**a_device)
        print("Current Prompt: " + net_connect.find_prompt())

        show_ver = net_connect.send_command("show version")
        print()
        print("#" * 80)
        print(show_ver)
        print("#" * 80)
        print()

        if "eos" in a_device["device_type"]:
            cmd = "show run"
        elif "juniper" in a_device["device_type"]:
            cmd = "show configuration"

        show_run = net_connect.send_command(cmd)
        filename = net_connect.base_prompt + ".txt"
        print("Save show run output: {}\n".format(filename))
        save_file(filename, show_run)


if __name__ == "__main__":
    main()
