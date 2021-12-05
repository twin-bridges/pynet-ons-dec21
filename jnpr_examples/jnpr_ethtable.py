from jnpr.junos import Device
from jnpr.junos.op.ethport import EthPortTable
from getpass import getpass
from rich import print
import pdbr # noqa

a_device = Device(host="srx1.lasthop.io", user="pyclass", password=getpass())
a_device.open()

# pdbr.set_trace()
ports = EthPortTable(a_device)
ports.get()

print(ports)
print(ports.keys())
print(ports.values())
print(ports.items())
