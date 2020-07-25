from owoify import Owoifator
from owoify.constants import kaomoji

owoifator = Owoifator()


def test_w():
    assert owoifator.owoify("Hello") == "Hewwo"
    assert owoifator.owoify("HELLO") == "HEWWO"


def test_nya():
    assert owoifator.owoify("Magni") == "Magnyi"
    assert owoifator.owoify("MAGNI") == "MAGNyI"


def test_d():
    assert owoifator.owoify("the") == "de"


def test_uv():
    assert owoifator.owoify("oven") == "uvn"


def test_kaomoji():
    assert owoifator.owoify("!")[1:] in kaomoji
