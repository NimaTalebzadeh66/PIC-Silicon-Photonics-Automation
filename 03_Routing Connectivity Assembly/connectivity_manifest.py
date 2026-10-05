
import json


connections = [
    {
        "from_instance": "input_0",
        "from_port": "o2",
        "to_instance": "device_0",
        "to_port": "o1",
    },
    {
        "from_instance": "input_1",
        "from_port": "o2",
        "to_instance": "device_1",
        "to_port": "o1",
    },
]

for connection in connections:
    print(connection)

with open("connectivity_manifest.json", "w") as f:
    json.dump(connections, f, indent=4)