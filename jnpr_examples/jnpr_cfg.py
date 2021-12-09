from jnpr.junos import Device
from jnpr.junos.utils.config import Config
from getpass import getpass
import pdbr

a_device = Device(host="vmx2.lasthop.io", user="pyclass", password=getpass())
a_device.open()
a_device.timeout = 120

cfg = Config(a_device)
cfg.lock()

pdbr.set_trace()
cfg.load("set system host-name test123", format="set", merge=True)
cfg.rollback(0)

cfg.load("set system host-name test123", format="set", merge=True)
print(cfg.diff())

cfg.commit()
# cfg.commit(comment="Testing from pyez")

cfg.load(path="test_config.conf", format="text", merge=True)
print(cfg.diff())
cfg.rollback(0)
cfg.unlock()
