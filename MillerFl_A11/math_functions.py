# math_functions.py
def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero!")
    return a / b


def power(a, b):
    if b == 0:
        return 1
    elif a == 0 and b < 0:
        raise ValueError("Undefined result: Cannot raise zero to a negative power.")
    else:
        return a ** b
