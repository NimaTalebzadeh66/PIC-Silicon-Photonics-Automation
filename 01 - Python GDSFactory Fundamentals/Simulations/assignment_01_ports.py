import gdsfactory as gf
from gdsfactory.gpdk import get_generic_pdk

get_generic_pdk().activate()

c = gf.Component("assignment_01_ports")

wg1 = c.add_ref(gf.components.straight(length=10))
wg2 = c.add_ref(gf.components.straight(length=25))
wg2.move((60, 30))

route = gf.routing.route_single(
    c,
    port1=wg1.ports["o2"],
    port2=wg2.ports["o1"],
    cross_section="strip",
    radius=16,
)
c.write_gds("assignment_01_ports.gds")

