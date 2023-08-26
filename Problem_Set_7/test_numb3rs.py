from numb3rs import validate


def test_validate_min():
    assert validate("0.0.0.0") == True


def test_validate_max():
    assert validate("255.255.255.255") == True


def test_validate_in_range():
    assert validate("127.0.0.1") == True


def test_validate_out_of_range():
    assert validate("-1.0.0.0") == False
    assert validate("0.0.0.-1") == False
    assert validate("275.0.0.0") == False
    assert validate("1.2.3.1000") == False
    assert validate("512.512.512.512") == False


def test_validate_incorrect_string():
    assert validate("cat") == False
    assert validate("a.0.0.0") == False
    assert validate("0.0.0.b") == False
