def add(a, b):
    try:
        return a + b
    except TypeError:
        raise TypeError("add() requires two numbers or compatible types")


def subtract(x, y):
    try:
        return x - y
    except TypeError:
        raise TypeError("subtract() requires two numbers or compatible types")


def multiply(a, b):
    try:
        return a * b
    except TypeError:
        raise TypeError("multiply() requires two numbers or compatible types")


def divide(a, b):
    try:
        if b == 0:
            raise ZeroDivisionError("divide() cannot divide by zero")
        return a / b
    except TypeError:
        raise TypeError("divide() requires two numbers")
