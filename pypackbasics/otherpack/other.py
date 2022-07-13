import numpy as np
import matplotlib.pyplot as plt

from .. import basics


def print_primes(max_prime, make_plot=False):
    finder = basics.PrimeFinder()
    finder.find_primes(max_prime, verbose=not make_plot)

    if make_plot:
        primes = finder.known_primes
        num_primes = len(primes)

        plt.scatter(np.arange(num_primes), np.log10(primes))
        plt.xlabel("n")
        plt.ylabel("$\\rm \\log(n^{th} \\; prime)$")
        plt.show()
