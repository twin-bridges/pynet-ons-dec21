from jnpr.junos import Device
from getpass import getpass
from rich import print

password = getpass()
vmx1 = {"host": "vmx1.lasthop.io", "user": "pyclass", "password": password}

a_device = Device(**vmx1)
a_device.open()
print(dict(a_device.facts))
