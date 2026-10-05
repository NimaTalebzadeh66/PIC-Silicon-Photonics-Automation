import gdsfactory as gf

@gf.cell
def custom_coupler(length=20, gap=0.20):
    c = gf.Component()
    coupler=gf.components.coupler(length=length,gap=gap)
    coupler_ref=c<<coupler

    c.add_port("o1", port=coupler_ref.ports["o1"])
    c.add_port("o2", port=coupler_ref.ports["o2"])
    c.add_port("o3", port=coupler_ref.ports["o3"])
    c.add_port("o4", port=coupler_ref.ports["o4"])

    return c