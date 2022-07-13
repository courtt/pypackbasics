import unittest

import pypackbasics


class TestPrimeFinder(unittest.TestCase):
    def test_find_primes_up_to_10(self):
        finder = pypackbasics.PrimeFinder()
        finder.find_primes(max_prime=10)
        print(finder.known_primes)
        assert finder.known_primes == [2, 3, 5, 7]
        assert finder.highest_check == 10
