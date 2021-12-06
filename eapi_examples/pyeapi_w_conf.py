import pyeapi
import pdbr

pdbr.set_trace()
device1 = pyeapi.connect_to("arista1")
device2 = pyeapi.connect_to("arista2")
print(device1)
