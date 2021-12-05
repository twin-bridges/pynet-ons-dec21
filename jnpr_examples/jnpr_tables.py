from jnpr.junos import Device
from jnpr.junos.op.arp import ArpTable
from rich import print
from getpass import getpass
import pdbr  # noqa

a_device = Device(host="vmx1.lasthop.io", user="pyclass", password=getpass())
a_device.open()

# pdbr.set_trace()
arp_entries = ArpTable(a_device)
arp_entries.get()
for k, v in arp_entries.items():
    print(k)
    print(v)
