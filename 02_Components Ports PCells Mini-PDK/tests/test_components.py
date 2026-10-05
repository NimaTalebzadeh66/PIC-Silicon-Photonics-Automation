import pytest
from gdsfactory.gpdk import get_generic_pdk
from pdk.components import pdk_straight
from components.tapers import taper_nima
from components.couplers import custom_coupler

get_generic_pdk().activate()


def test_pdk_straight_has_two_ports():
    k = pdk_straight(length=20, width=0.5)

    assert len(k.ports) == 2


def test_pdk_straight_rejects_negative_width():
    with pytest.raises(ValueError):
        pdk_straight(length=20, width=-0.5)

def test_pdk_straight_deterministic_name():
    a = pdk_straight(length=20, width=0.5)
    b = pdk_straight(length=20, width=0.5)

    assert a.name == b.name

from pdk.layers import WG


def test_pdk_straight_port_names():
    c = pdk_straight(length=20, width=0.5)

    assert "o1" in c.ports
    assert "o2" in c.ports


def test_pdk_straight_port_layer():
    c = pdk_straight(length=20, width=0.5)

    assert tuple(c.ports["o1"].layer) == WG
    assert tuple(c.ports["o2"].layer) == WG

def test_taper_amjuk_ports():
    m = taper_nima(
        width1=0.45,
        width2=1.0,
        taper_length=15,
    )

    assert len(m.ports) == 2
    assert "A_in" in m.ports
    assert "A_out" in m.ports

def test_coupler_custom_coupler():
    p=custom_coupler(length=20,gap=0.2)
    assert len(p.ports) == 4
    assert "o1" in p.ports
    assert "o2" in p.ports
    assert "o3" in p.ports
    assert "o4" in p.ports