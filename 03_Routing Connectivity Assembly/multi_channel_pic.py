import json
import gdsfactory as gf

gf.gpdk.PDK.activate()


@gf.cell
def channel_device(length=40):
    c = gf.Component()

    wg = c << gf.components.straight(length=length)

    c.add_ports(wg.ports)

    return c


@gf.cell
def multi_channel_pic():
    c = gf.Component()

    device_lengths = [40, 60, 80, 100]
    pitch = 30

    inputs = []
    devices = []

    for i, length in enumerate(device_lengths):
        inp = c << gf.components.straight(length=20)
        inp.move((0, i * pitch))
        inputs.append(inp)

        dev = c << channel_device(length=length)
        dev.move((100, i * pitch))
        devices.append(dev)

    routes = gf.routing.route_bundle(
        c,
        ports1=[ref.ports["o2"] for ref in inputs],
        ports2=[ref.ports["o1"] for ref in devices],
        cross_section="strip",
    )

    for i, inp in enumerate(inputs):
        c.add_port(
            name=f"in{i}",
            port=inp.ports["o1"],
        )

    for i, dev in enumerate(devices):
        c.add_port(
            name=f"out{i}",
            port=dev.ports["o2"],
        )
    c.info["n_devices"] = len(devices)
    c.info["n_routes"] = len(routes)
    return c



if __name__ == "__main__":
    c = multi_channel_pic()

    connections = []

    for i in range(4):
        connections.append(
            {
                "from_instance": f"input_{i}",
                "from_port": "o2",
                "to_instance": f"device_{i}",
                "to_port": "o1",
            }
        )

    with open("connectivity_manifest.json", "w") as f:
        json.dump(connections, f, indent=4)

    c.write_gds("multi_channel_pic.gds")
    c.show()