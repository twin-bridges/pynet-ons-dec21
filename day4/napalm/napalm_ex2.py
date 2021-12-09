#!/usr/bin/env python
from napalm import get_network_driver
from my_devices import arista1, arista2, arista3, arista4


if __name__ == "__main__":

    vlan_file = "vlan-cfg.txt"

    for device in (arista1, arista2, arista3, arista4):
        driver = get_network_driver("eos")
        conn = driver(**device)
        conn.open()

        # Stage the config change
        conn.load_merge_candidate(filename=vlan_file)
        diff = conn.compare_config()

        # View the diff
        print("\n\n")
        print(f"Configuring: {conn.hostname}")
        print()
        print("--- Diff ---")
        print(diff)
        print("--- End Diff ---")

        # Commit the change
        if diff:
            print("\n\nCommitting VLAN change")
            conn.commit_config()
        else:
            print("\n\nNo changes.")
        print("\n\n")
        conn.close()
