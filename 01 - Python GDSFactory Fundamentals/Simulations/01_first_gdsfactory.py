import gdsfactory as gf
from gdsfactory.gpdk import get_generic_pdk

get_generic_pdk().activate()

c = gf.Component("connected_waveguides")

wg1 = c.add_ref(gf.components.straight(length=10))
wg2 = c.add_ref(gf.components.straight(length=20))

wg2.connect("o1", wg1.ports["o2"])

c.write_gds("connected_waveguides.gds")