from unittest import TestCase


def func(a):
    if a % 2 == 0:
        return 2 * a
    else:
        return a / 2


print("Func: ", func(3))

TestCase().assertEqual(func(3), 31.5, "Expected value and actual value are not equal")
