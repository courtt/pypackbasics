import unittest

import pypackbasics
from pypackbasics.utilpack.utils import check_divisibility


class TestPrimeFinder(unittest.TestCase):
    def test_find_primes_up_to_10(self):
        finder = pypackbasics.PrimeFinder()
        finder.find_primes(max_prime=10)
        assert finder.known_primes == [2, 3, 5, 7]
        assert finder.highest_check == 10

    def test_divisibility(self):
        value = 32
        divisors = [2,4,8,16]
        assert pypackbasics.utilpack.check_divisibility(value,divisors)
        divisors = [3]
        assert pypackbasics.utilpack.check_divisibility(value,divisors)

