import pytest
from working import convert


def test_convert_incorrect_value():
    with pytest.raises(ValueError):
        convert("incorrect value")


def test_convert_epmty():
    with pytest.raises(ValueError):
        convert("")


def test_convert_no_minutes():
    convert("9 AM to 5 PM") == "9:00 to 17:00"
    convert("9 PM to 5 AM") == "21:00 to 5:00"


def test_convert_with_minutes():
    convert("9:00 AM to 5:00 PM") == "9:00 to 17:00"
    convert("9:00 PM to 5:00 AM") == "21:00 to 5:00"
