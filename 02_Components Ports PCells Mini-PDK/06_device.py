import gdsfactory as gf
from gdsfactory.gpdk import get_generic_pdk

get_generic_pdk().activate()


@gf.cell
def taper_amjuk(
    width1=0.45,
    width2=1.0,
    length1=10,
    length2=20,
    taper_length=15,
):
    c = gf.Component()

    wg1 = gf.components.straight(length=length1, width=width1)
    wg2 = gf.components.straight(length=length2, width=width2)
    taper = gf.components.taper(
        width1=width1,
        width2=width2,
        length=taper_length,
    )

    wg1_ref = c << wg1
    taper_ref = c << taper
    wg2_ref = c << wg2

    taper_ref.connect("o1", wg1_ref.ports["o2"])
    wg2_ref.connect("o1", taper_ref.ports["o2"])

    c.add_port("A_in", port=wg1_ref.ports["o1"])
    c.add_port("A_out", port=wg2_ref.ports["o2"])

    return c


d1 = taper_amjuk(
    width1=0.45,
    width2=1.0,
    length1=10,
    length2=20,
    taper_length=15,
)

d2 = taper_amjuk(
    width1=0.45,
    width2=1.0,
    length1=10,
    length2=20,
    taper_length=15,
)

d3 = taper_amjuk(
    width1=0.45,
    width2=1.0,
    length1=10,
    length2=20,
    taper_length=25,
)

print(d1.name)
print(d2.name)
print(d3.name)