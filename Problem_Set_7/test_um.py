from um import count


def test_cont_single_um():
    assert count("um") == 1
    assert count(" um ") == 1
    assert count("um?") == 1


def test_um_in_sentence():
    assert count("Um, thanks for the album") == 1
    assert count("Um, thanks, um...") == 2


def test_count_um_in_word():
    assert count("yum") == 0
    assert count("yummy") == 0
