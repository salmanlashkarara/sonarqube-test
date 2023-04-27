from app.main import *


def test_even_number():
    assert func(2) == 4


def test_odd_number():
    assert func(3) == 1.5


def test_sum():
    assert sum(3, 2) == 5


def test_sub():
    assert sub(3, 2) == 1


def test_div():
    assert div(6, 2) == 3


def test_multitude():
    assert multitude(6, 2) == 12


def test_power():
    assert power(6, 2) == 36
