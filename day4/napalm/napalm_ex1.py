#!/usr/bin/env python
"""
Arista device definitions are stored in external Python module so that they can
be re-used in both exercises.
"""
from rich import print
from napalm import get_network_driver
from my_devices import arista1, arista2, arista3, arista4


if __name__ == "__main__":
    print()
    for device in [arista1, arista2, arista3, arista4]:
        driver = get_network_driver("eos")
        with driver(**device) as device:
            device.open()
            vlans = device.get_vlans()
            host = device.hostname

        print()
        print("-" * 80)
        print(f"Host: {host}")
        print("-" * 12)
        print(vlans)
        print("-" * 80)
        print()

    print()
