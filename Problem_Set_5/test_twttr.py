from twttr import shorten


def test_empty_shorten():
    assert shorten("aeiou") == ""
    assert shorten("AEIOU") == ""


def test_shorten():
    assert shorten("test") == "tst"
    assert shorten("TEST") == "TST"
