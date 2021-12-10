from jnpr.junos import Device
from jnpr.junos.utils.config import Config
from jnpr.junos.exception import LockError
from getpass import getpass
import pdbr

password = getpass()
vmx1 = {"host": "vmx2.lasthop.io", "user": "pyclass", "password": password}

a_device = Device(**vmx1)
a_device.open()
a_device.timeout = 120

cfg = Config(a_device)
print("Locking configuration")
cfg.lock()

try:
    cfg.lock()
except LockError:
    print("We tried to lock a second time...and caught the exception")

pdbr.set_trace()
cfg.load("set system host-name vmx2", format="set", merge=True)

print()
print(cfg.diff())
print()

print("\nCommit config change")
cfg.commit()
cfg.unlock()
