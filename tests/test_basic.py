from app.main import *


def test_even_number():
    assert func(2) == 4


def test_odd_number():
    assert func(3) == 1.5


def test_sum():
    assert sum(3, 2) == 5


def test_sub():
    assert sub(3, 2) == 1
