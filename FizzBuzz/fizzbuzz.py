import math


def fizzbuzz(n: int, a: int = 3, b: int = 5) -> str:
    """Fizz Buzz function
    >>> fizzbuzz(12,4,2)
    'FizzBuzz'
    >>> fizzbuzz(2,6,1)
    'Buzz'
    >>> fizzbuzz(1,3,3)
    '1'
    """
    if n % (a * b / math.gcd(a, b)) == 0: return "FizzBuzz"
    if n % a == 0: return "Fizz"
    if n % b == 0: return "Buzz"
    return str(n)
