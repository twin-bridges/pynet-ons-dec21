#!/usr/bin/env python
from getpass import getpass
from napalm import get_network_driver


if __name__ == "__main__":
    host = "cisco3.lasthop.io"
    username = "pyclass"
    password = getpass()
    optional_args = {}

    driver = get_network_driver("ios")
    device = driver(host, username, password, optional_args=optional_args)

    print()
    print(">>>Test device open")
    device.open()

    print()
    print(">>>Load config change (replace)")
    device.load_replace_candidate(filename="cisco3.txt")
    print(device.compare_config())
    # device.discard_config()
    # device.commit_config()
    # device.rollback()
