from app.main import func


def test_even_number():
    assert func(2) == 4


def test_odd_number():
    assert func(3) == 1.5
