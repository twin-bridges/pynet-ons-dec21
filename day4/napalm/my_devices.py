# Store Arista device definitions in an external Python module so that I
# can re-use them in both of the exercises
from getpass import getpass


password = getpass()

arista1 = {
    "hostname": "arista1.lasthop.io",
    "username": "pyclass",
    "password": password,
    "optional_args": {},
}

arista2 = {
    "hostname": "arista2.lasthop.io",
    "username": "pyclass",
    "password": password,
    "optional_args": {},
}

arista3 = {
    "hostname": "arista3.lasthop.io",
    "username": "pyclass",
    "password": password,
    "optional_args": {},
}

arista4 = {
    "hostname": "arista4.lasthop.io",
    "username": "pyclass",
    "password": password,
    "optional_args": {},
}
