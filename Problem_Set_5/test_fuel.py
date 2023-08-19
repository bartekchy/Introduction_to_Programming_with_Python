import pytest
from fuel import gauge
from fuel import convert


def test_convert_not_int():
    with pytest.raises(ValueError):
        convert("12.2/12.2")


def test_convert_zero_division():
    with pytest.raises(ZeroDivisionError):
        convert("10/0")


def test_guage_full():
    assert gauge(0) == "E"
    assert gauge(1) == "E"


def test_guage_empty():
    assert gauge(100) == "F"
    assert gauge(99) == "F"


def test_guage_default():
    assert gauge(50) == "50%"
