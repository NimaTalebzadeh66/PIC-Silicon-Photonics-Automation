import gdsfactory as gf

gf.gpdk.PDK.activate()


@gf.cell
def input_block():
    c = gf.Component()

    wg = c << gf.components.straight(length=50)

    c.add_port(
        name="o1",
        port=wg.ports["o1"],
    )

    c.add_port(
        name="o2",
        port=wg.ports["o2"],
    )

    return c


@gf.cell
def device_block():
    c = gf.Component()

    mmi = c << gf.components.mmi1x2()

    c.add_ports(mmi.ports)

    return c

@gf.cell
def top_circuit():
    c = gf.Component()

    inp = c << input_block()
    dev = c << device_block()

    dev.move((120, 0))
    gf.routing.route_single(
        c,
        port1=inp.ports["o2"],
        port2=dev.ports["o1"],
        cross_section="strip",
    )
    c.add_port("o1", port=inp.ports["o1"])
    c.add_port("o2", port=dev.ports["o2"])
    c.add_port("o3", port=dev.ports["o3"])
    return c

if __name__ == "__main__":
    c = top_circuit()
    c.write_gds("hierarchical_circuit.gds")
    c.show()