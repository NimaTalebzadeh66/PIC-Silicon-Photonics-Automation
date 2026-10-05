import gdsfactory as gf
@gf.cell
def custom_waveguid(length=20, width=0.5):
    c=gf.Component()
    wg1=gf.components.straight(length=length, width=width)
    wg_ref=c<<wg1

    c.add_port("A_in", port=wg_ref.ports["o1"])
    c.add_port("A_out", port=wg_ref.ports["o2"])

    return c
