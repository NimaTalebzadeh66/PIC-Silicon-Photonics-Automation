import gdsfactory as gf
from pdk.cross_sections import strip_xs


@gf.cell
def pdk_straight(length=20, width=0.5):
    c = gf.Component()

    wg = gf.components.straight(
        length=length,
        cross_section=strip_xs(width=width),
    )

    wg_ref = c << wg

    c.add_port("o1", port=wg_ref.ports["o1"])
    c.add_port("o2", port=wg_ref.ports["o2"])

    return c