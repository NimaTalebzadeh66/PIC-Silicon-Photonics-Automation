import gdsfactory as gf
from gdsfactory.gpdk import get_generic_pdk

get_generic_pdk().activate()

c = gf.Component()

widths = [0.45, 0.50, 0.60]

for i, width in enumerate(widths):
    xs = gf.cross_section.strip(width=width)

    wg = gf.components.straight(
        length=20,
        cross_section=xs,
    )

    wg_ref = c << wg
    wg_ref.movey(i * 10)

print(c)

from pathlib import Path

path = c.write_gds("waveguide_array.gds")
print(Path(path).resolve())