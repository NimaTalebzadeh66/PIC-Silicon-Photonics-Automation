import gdsfactory as gf
from gdsfactory.gpdk import get_generic_pdk

get_generic_pdk().activate()

def make_bent_waveguide(length1=15, length2=20):
    c = gf.Component("assignment_06_parameterized")

    wg1 = c.add_ref(gf.components.straight(length=length1))
    bend = c.add_ref(gf.components.bend_euler())
    wg2 = c.add_ref(gf.components.straight(length=length2))

    bend.connect("o1", wg1.ports["o2"])
    wg2.connect("o1", bend.ports["o2"])

    c.add_port("o1", port=wg1.ports["o1"])
    c.add_port("o2", port=wg2.ports["o2"])

    return c

device = make_bent_waveguide(25, 80)
device.write_gds("assignment_06_parameterized.gds")