import gdsfactory as gf
from gdsfactory.gpdk import get_generic_pdk
from pdk.components import pdk_straight

get_generic_pdk().activate()

device = pdk_straight(
    length=30,
    width=0.6,
)

gds_path = device.write_gds("pdk_straight.gds")
oas_path = device.write("pdk_straight.oas")

print("GDS written to:", gds_path)
print("OAS written to:", oas_path)

from pathlib import Path

gds_file = Path("pdk_straight.gds")
oas_file = Path("pdk_straight.oas")

print("GDS exists:", gds_file.exists())
print("OAS exists:", oas_file.exists())

if gds_file.exists():
    print("GDS size:", gds_file.stat().st_size, "bytes")

if oas_file.exists():
    print("OAS size:", oas_file.stat().st_size, "bytes")