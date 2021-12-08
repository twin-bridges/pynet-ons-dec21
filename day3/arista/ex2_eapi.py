import pyeapi
from getpass import getpass
from rich import print


cfg = [
    "vlan 800",
    "name blue800",
    "vlan 801",
    "name blue801",
    "vlan 802",
    "name blue802",
]

connection = pyeapi.client.connect(
    transport="https",
    host="arista1.lasthop.io",
    username="pyclass",
    password=getpass(),
    port="443",
)

device = pyeapi.client.Node(connection)
cfg_output = device.config(cfg)

output = device.enable(["show vlan"])
print(output)
