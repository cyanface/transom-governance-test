from p01_20260921t032500_p01_r03 import bump


def test_bump_zero():
    assert bump(0) == 1


def test_bump_negative():
    assert bump(-3) == -2


def test_bump_positive():
    assert bump(4) == 5
