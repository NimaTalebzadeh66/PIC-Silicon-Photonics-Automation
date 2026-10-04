import gdsfactory as gf
from pdk.layers import WG

def strip_xs (width = 0.5):
    return gf.cross_section.strip(width=width, layer=WG,)


