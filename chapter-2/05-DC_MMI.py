
import gdsfactory as gf
from gdsfactory.gpdk import get_generic_pdk

get_generic_pdk().activate()
mmi = gf.components.mmi1x2()
print(mmi)
mmi.pprint_ports()
mmi.write_gds("mmi1x2.gds")