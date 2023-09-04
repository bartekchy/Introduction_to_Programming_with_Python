from seasons import minutes_from_birth
import pytest


def test_minutes_from_birth_default():
    # work only if you type a date two years ago from today (today is 2023-08-27)
    assert (
        minutes_from_birth("2021-08-27")
        == "one million, fifty-one thousand, two hundred minutes"
    )
