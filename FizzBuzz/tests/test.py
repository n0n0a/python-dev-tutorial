from unittest import TestCase
from FizzBuzz.fizzbuzz import fizzbuzz


class TestFizzBuzz(TestCase):
    def test_fizzbuzz(self):
        self.assertEqual(fizzbuzz(12), "Fizz")
        self.assertEqual(fizzbuzz(4,9,13), "4")
        self.assertEqual(fizzbuzz(12,2,6), "FizzBuzz")
        self.assertEqual(fizzbuzz(22,7,5), "22")
