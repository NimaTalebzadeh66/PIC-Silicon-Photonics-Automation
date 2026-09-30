import gdsfactory as gf
from gdsfactory.gpdk import get_generic_pdk

get_generic_pdk().activate()

top = gf.Component("assignment_09_top_level")

@gf.cell
def make_bent_waveguide(length1=15, length2=25):
   c=gf.Component()
   wg1 = c.add_ref(gf.components.straight(length=length1))
   bend = c.add_ref(gf.components.bend_euler())
   wg2 = c.add_ref(gf.components.straight(length=length2))

   bend.connect("o1",wg1.ports["o2"])
   wg2.connect("o1",bend.ports["o2"])

   c.add_port("o1",port=wg1.ports["o1"])
   c.add_port("o2",port=wg2.ports["o2"])

   return c


device1 = make_bent_waveguide(length1=10, length2=20)
device2 = make_bent_waveguide(length1=25, length2=80)
ref1 = top.add_ref(device1)
ref2 = top.add_ref(device2)
ref2.move((10,0))

print(top)


top.write_gds("assignment_09_top_level.gds")

