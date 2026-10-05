import gdsfactory as gf

gf.gpdk.PDK.activate()


@gf.cell
def bundle_demo():
    c = gf.Component()

    inputs = []
    outputs = []

    for i in range(4):
        wg_in = c << gf.components.straight(length=20)
        wg_in.move((0, i * 20))
        inputs.append(wg_in)

        wg_out = c << gf.components.straight(length=20)
        wg_out.move((200, i * 20))
        outputs.append(wg_out)

    # Move only the last output 40 µm farther right
    outputs[-1].move((40, 0))

    routes = gf.routing.route_bundle(
        c,
        ports1=[ref.ports["o2"] for ref in inputs],
        ports2=[ref.ports["o1"] for ref in outputs],
        cross_section="strip",
    )

    for i, route in enumerate(routes):
        print(i, route.length)

    return c
if __name__ == "__main__":
    c = bundle_demo()
    c.write_gds("bundle_routing.gds")
    c.show()