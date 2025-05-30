def add(a, b):
    """
    Returns the sum of a and b.

    :param a: The first number (int or float).
    :param b: The second number (int or float).
    :returns: The result of a + b.
    """
    return a + b

def subtract(a, b):
    """
    Returns the result of subtracting b from a.

    :param a: The number to subtract from (int or float).
    :param b: The number to subtract (int or float).
    :returns: The result of a - b.
    """
    return a - b

def multiply(a, b):
    """
    Returns the product of a and b.

    :param a: The first factor (int or float).
    :param b: The second factor (int or float).
    :returns: The result of a * b.
    """
    return a * b

def divide(a, b):
    """
    Returns the result of dividing a by b.

    :param a: The numerator (int or float).
    :param b: The denominator (int or float).
    :returns: The result of a / b.
    :raises ValueError: If b is zero.
    """
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b
