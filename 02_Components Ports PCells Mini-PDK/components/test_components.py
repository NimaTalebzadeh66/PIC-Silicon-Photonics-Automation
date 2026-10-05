import gdsfactory as gf
from gdsfactory.gpdk import get_generic_pdk
from couplers import custom_coupler

get_generic_pdk().activate()

device = custom_coupler(gap=0.2, length=20,)

print(device)
device.pprint_ports()
device.write_gds("custom_coupler.gds")