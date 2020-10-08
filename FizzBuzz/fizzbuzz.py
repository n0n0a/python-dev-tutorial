def fizzbuzz(n: int) -> str:
    """Fizz Buzz function
    >>> fizzbuzz(3)
    'Fizz'
    >>> fizzbuzz(5)
    'Buzz'
    >>> fizzbuzz(15)
    'FizzBuzz'
    >>> fizzbuzz(7)
    '7'
    """
    if n%15==0: return "FizzBuzz"
    if n%3==0: return "Fizz"
    if n%5==0: return "Buzz"
    return str(n)