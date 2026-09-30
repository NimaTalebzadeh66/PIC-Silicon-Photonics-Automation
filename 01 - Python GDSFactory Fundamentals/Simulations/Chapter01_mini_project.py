import gdsfactory as gf
from gdsfactory.gpdk import get_generic_pdk
get_generic_pdk().activate()

top = gf.Component("chapter01_mini_project")

@gf.cell
def make_bent_waveguide(length1=10,length2=20):
    c = gf.Component()
    wg1 = c.add_ref(gf.components.straight(length=length1))
    bend = c.add_ref(gf.components.bend_euler())
    wg2 = c.add_ref(gf.components.straight(length=length2))

    bend.connect("o1",wg1.ports["o2"])
    wg2.connect("o1", bend.ports["o2"])

    c.add_port("o1", port=wg1.ports["o1"])
    c.add_port("o2", port=wg2.ports["o2"])
    return c

device1=make_bent_waveguide(length1=20, length2=35)
device2=make_bent_waveguide(length1=40, length2=60)
ref1=top.add_ref(device1)
ref2=top.add_ref(device2)
ref2.move((100,40))

top.add_port("A_in", port=ref1.ports["o1"])
top.add_port("A_out", port=ref1.ports["o2"])
top.add_port("B_in", port=ref2.ports["o1"])
top.add_port("B_out", port=ref2.ports["o2"])

print(list(top.ports))
print(top.bbox())
top.write_gds("chapter01_mini_project.gds")
