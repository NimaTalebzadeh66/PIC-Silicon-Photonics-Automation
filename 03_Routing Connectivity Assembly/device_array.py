import gdsfactory as gf

gf.gpdk.PDK.activate()


@gf.cell
def device_array():
    c = gf.Component()

    devices = [
        {"length": 20},
        {"length": 40},
        {"length": 60},
        {"length": 80},
    ]
    pitch = 30
    for i, params in enumerate(devices):
        wg = c << gf.components.straight(length=params["length"])
        wg.move((0, i * pitch))


    return c

if __name__ == "__main__":
    c = device_array()
    c.write_gds("device_array.gds")
    c.show()