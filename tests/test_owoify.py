from owoify import owoify
from owoify.constants import kaomoji


def test_w():
    assert owoify("Hello") == "Hewwo"
    assert owoify("HELLO") == "HEWWO"


def test_nya():
    assert owoify("Magni") == "Magnyi"
    assert owoify("MAGNI") == "MAGNyI"


def test_d():
    assert owoify("the") == "de"


def test_uv():
    assert owoify("oven") == "uvn"


def test_kaomoji():
    assert owoify("!")[1:] in kaomoji
