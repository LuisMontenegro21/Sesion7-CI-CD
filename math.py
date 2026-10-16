def square(n):
    """Return the squares of a and b as a pair."""
    if not (isinstance(n, int) or  isinstance(n, float)):
        raise TypeError("n must be int or float")
    return n**n


def factorial(n):
    """Return n!, raising ValueError for negative integers."""
    if not isinstance(n, int) or isinstance(n, bool):
        raise TypeError("n must be an integer")
    if n < 0:
        raise ValueError("n must be non-negative")

    result = 1
    for factor in range(2, n + 1):
        result *= factor
    return result


def is_prime(n):
    """Return whether n is a prime integer."""
    if not isinstance(n, int) or isinstance(n, bool):
        raise TypeError("n must be an integer")
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2

    divisor = 3
    while divisor * divisor <= n:
        if n % divisor == 0:
            return False
        divisor += 2
    return True


def gcd(a, b):
    """Return the greatest common divisor of two integers."""
    if (
        not isinstance(a, int)
        or isinstance(a, bool)
        or not isinstance(b, int)
        or isinstance(b, bool)
    ):
        raise TypeError("a and b must be integers")

    a, b = abs(a), abs(b)
    while b:
        a, b = b, a % b
    return a


def lcm(a, b):
    """Return the least common multiple of two integers."""
    if (
        not isinstance(a, int)
        or isinstance(a, bool)
        or not isinstance(b, int)
        or isinstance(b, bool)
    ):
        raise TypeError("a and b must be integers")
    if a == 0 or b == 0:
        return 0
    return abs(a // gcd(a, b) * b)