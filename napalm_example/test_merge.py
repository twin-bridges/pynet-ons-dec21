#!/usr/bin/env python
from getpass import getpass
from napalm import get_network_driver

import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


if __name__ == "__main__":
    host = "nxos1.lasthop.io"
    username = "pyclass"
    password = getpass()
    optional_args = {"port": 8443}

    driver = get_network_driver("nxos")
    device = driver(host, username, password, optional_args=optional_args)

    device.open()
    device.load_merge_candidate(filename="nxos-merge.conf")
    print(device.compare_config())

    device.discard_config()
    print("--- Diff ---")
    print(device.compare_config())
    print("--- End Diff ---")

    print(">>>Load config change (merge) - commit")
    device.load_merge_candidate(filename="nxos-merge.conf")
    device.commit_config()

    device.rollback()
