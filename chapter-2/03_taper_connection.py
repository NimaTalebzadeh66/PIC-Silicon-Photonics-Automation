import gdsfactory as gf
from gdsfactory.gpdk import get_generic_pdk

get_generic_pdk().activate()

c = gf.Component()

wg1=gf.components.straight (length=10, width=0.45)
taper1=gf.components.taper(width1=0.45, length=10,width2=1)
wg2 = gf.components.straight (length=10, width=1)


wg1_ref= c<<wg1
wg2_ref= c<<wg2
taper1_ref= c<<taper1

taper1_ref.connect("o1",wg1_ref.ports["o2"])
wg2_ref.connect("o1",taper1_ref.ports["o2"])

c.write_gds("taper_connection.gds")