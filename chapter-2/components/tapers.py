import gdsfactory as gf

@gf.cell
def taper_nima(
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
    if width1 <= 0 or width2 <= 0:
        raise ValueError("Widths must be positive")

    if length1 <= 0 or length2 <= 0 or taper_length <= 0:
        raise ValueError("Lengths must be positive")

    return c