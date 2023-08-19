from plates import is_valid


def test_is_valid_length():
    assert is_valid("tooLong") == False
    assert is_valid("right") == True


def test_is_valid_numbers():
    assert is_valid("12abcd") == False
    assert is_valid("ab12cd") == False
    assert is_valid("abcd12") == True


def test_is_valid_whitespaces():
    assert is_valid(" abcd") == False
    assert is_valid("ab cd") == False
    assert is_valid("abcd ") == False
    assert is_valid("abcd") == True


def test_is_valid_default():
    assert is_valid("") == False
