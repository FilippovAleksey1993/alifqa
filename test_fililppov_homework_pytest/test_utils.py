from utils import is_even


def test_4():
    assert is_even(4) == True


def test_7():
    assert is_even(7) == False


def test_0():
    assert is_even(0) == True
