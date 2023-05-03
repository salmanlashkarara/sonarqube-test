def func(a):
    if a % 2 == 0:
        return 2 * a
    else:
        return a / 2


def sum(a, b):
    return a + b


def sub(a, b):
    return a - b


def div(a, b):
    return a / b


def multitude(a, b):
    return a * b


def power(a, b):
    return a ** b


def sum_list(lst):
    print("Hellllo!!!!")
    total = 0
    for num in lst:
        total += num
    return total


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
