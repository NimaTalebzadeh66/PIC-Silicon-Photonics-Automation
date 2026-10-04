import gdsfactory as gf
from gdsfactory.gpdk import get_generic_pdk

from pdk.components import pdk_straight
from components.tapers import taper_nima
from components.couplers import custom_coupler
from pdk.cross_sections import strip_xs
get_generic_pdk().activate()

gallery = gf.Component("chapter2_component_gallery")

straight = pdk_straight(length=30, width=0.5)


taper = taper_nima(
    width1=0.45,
    width2=1.0,
    taper_length=15,
)

coupler = custom_coupler(
    gap=0.2,
    length=20,
)

bend = gf.components.bend_euler(radius=10)

mmi = gf.components.mmi1x2()
bend_ref = gallery << bend
mmi_ref = gallery << mmi


straight_ref = gallery << straight
taper_ref = gallery << taper
coupler_ref = gallery << coupler

taper_ref.movey(-30)
coupler_ref.movey(-70)
bend_ref.move((60, 0))
mmi_ref.move((60, -40))

wg_a = gf.components.straight(length=10, width=0.5)
wg_b = gf.components.straight(length=10, width=0.5)

wg_a_ref = gallery << wg_a
wg_b_ref = gallery << wg_b

wg_b_ref.move((30, 50))

routing = gf.routing.route_single(
    gallery,
    port1=wg_a_ref.ports["o2"],
    port2=wg_b_ref.ports["o1"],
    cross_section=strip_xs(width=0.5),
)
gallery.write_gds("chapter2_component_gallery.gds")