import pyeapi
from getpass import getpass
import pdbr


pdbr.set_trace()
connection = pyeapi.client.connect(
    transport="https",
    host="arista1.lasthop.io",
    username="pyclass",
    password=getpass(),
    port="443",
)

# enable = getpass("Enable: ")
# device = pyeapi.client.Node(connection, enablepwd=enable)
device = pyeapi.client.Node(connection)
