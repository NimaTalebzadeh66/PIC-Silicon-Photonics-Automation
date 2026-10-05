import sys
from importlib.metadata import version

print("Python interpreter:", sys.executable)
print("GDSFactory version:", version("gdsfactory"))