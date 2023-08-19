from bank import value


def test_value_hello():
    assert value("hello, david") == "$0"
    assert value(" hello") == "$0"


def test_value_h():
    assert value("h, david") == "$20"
    assert value(" h") == "$20"
    assert value("home") == "$20"
    assert value("he,llo") == "$20"


def test_value_default():
    assert value("asdfs") == "$100"
    assert value("") == "$100"
