import math
import argparse
import sys
import click

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

@click.command()
@click.argument("nums", nargs = -1, type = int)
@click.option("--fizz", type=int, default=3, help="Number corresponds to Fizz.")
@click.option("--buzz", type=int, default=5, help="Number corresponds to Buzz.")
def main(nums, fizz, buzz):
    if nums:  # 数字の列が引数から渡された場合には、それらの数字にFizzBuzzを適用する
        sys.stderr.write("Reading numbers from arguments ...\n")
        for n in nums:
            sys.stdout.write(f"{fizzbuzz(n, fizz=fizz, buzz=buzz)}\n")
    else:  # 数字の列が引数から渡されなかった場合には、標準入力から数字を読み込む
        sys.stderr.write("Reading numbers from stdin ...\n")
        try:
            line = sys.stdin.readline()
            while line:
                sys.stdout.write(f"{fizzbuzz(int(line), fizz=fizz, buzz=buzz)}\n")
                line = sys.stdin.readline()
        except KeyboardInterrupt:
            return