import pyeapi
from getpass import getpass
from rich import print

connection = pyeapi.client.connect(
    transport="https",
    host="arista1.lasthop.io",
    username="pyclass",
    password=getpass(),
    port="443",
)

cfg = ["vlan 225", "name green", "vlan 226", "name red"]
device = pyeapi.client.Node(connection)
output = device.config(cfg)
print(output)
