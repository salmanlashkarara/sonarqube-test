from unittest import TestCase


def func(a):
    if a % 2 == 0:
        return 2 * a
    else:
        return a / 2


print("Func: ", func(3))

TestCase().assertEqual(func(3), 2.5,
                       "Expected value {actual_value} and actual value {expected_value} are not equal".format(
                           actual_value=func(3), expected_value=1.5))

TestCase().assertEqual(func(2), 4,
                       "Expected value {actual_value} and actual value {expected_value} are not equal".format(
                           actual_value=func(2), expected_value=4))
