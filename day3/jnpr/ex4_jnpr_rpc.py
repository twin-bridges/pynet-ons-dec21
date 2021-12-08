#!/usr/bin/env python
from jnpr.junos import Device
from lxml import etree
from getpass import getpass

password = getpass()
device = {"host": "vmx1.lasthop.io", "user": "pyclass", "password": password}

a_device = Device(**device)
a_device.open()

# show interfaces terse | display xml rpc
# <get-interface-information>
# convert the hyphens to underscores

xml_out = a_device.rpc.get_interface_information()
print(etree.tostring(xml_out, encoding="unicode", pretty_print=True))
