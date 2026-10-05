from hierarchical_circuit import top_circuit
from multi_channel_pic import multi_channel_pic


def test_top_circuit_ports():
    c = top_circuit()

    assert len(c.ports) == 3
    assert {port.name for port in c.ports} == {"o1", "o2", "o3"}
    assert len(c.insts) == 3


def test_multi_channel_counts():
    c = multi_channel_pic()

    assert c.info["n_devices"] == 4
    assert c.info["n_routes"] == 4

    assert len(c.ports) == 8
    assert {port.name for port in c.ports} == {
        "in0", "in1", "in2", "in3",
        "out0", "out1", "out2", "out3",
    }