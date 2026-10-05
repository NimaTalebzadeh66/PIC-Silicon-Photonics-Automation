import gdsfactory as gf

gf.gpdk.PDK.activate()

@gf.cell
def placement_demo():
    c = gf.Component()

    dev1 = c << gf.components.mmi1x2()
    for port in dev1.ports:
        print(port.name, port.center, port.orientation)
    dev2 = c << gf.components.mmi1x2()
    dev2.move((100, 40.625))
    dev2.rotate(180)
    route = gf.routing.route_single(
     c,
     port1=dev1.ports["o2"],
     port2=dev2.ports["o1"],
     cross_section="strip",
     radius=20,


    )
    print("Route length:", route.length)
    return c
if __name__ == "__main__":
    c = placement_demo()
    c.write_gds("placement_vs_routing.gds")
    c.show()