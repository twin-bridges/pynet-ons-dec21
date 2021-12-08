import pyeapi
from getpass import getpass
from rich import print

password = getpass()
base_dict = {
    "transport": "https",
    "username": "pyclass",
    "password": password,
    "port": "443",
}

arista1 = base_dict.copy()
arista1["host"] = "arista1.lasthop.io"
arista2 = base_dict.copy()
arista2["host"] = "arista2.lasthop.io"
arista3 = base_dict.copy()
arista3["host"] = "arista3.lasthop.io"
arista4 = base_dict.copy()
arista4["host"] = "arista4.lasthop.io"

print()
for device_dict in (arista1, arista2, arista3, arista4):
    conn = pyeapi.client.connect(**device_dict)
    device = pyeapi.client.Node(conn)
    output = device.enable(["show lldp neighbors"])
    print()
    print(f"Host: {device_dict['host']}")
    print(output[0]["result"]["lldpNeighbors"])
    print("-" * 80)
print()
