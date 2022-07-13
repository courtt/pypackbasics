from .utilpack.utils import check_divisibility


class PrimeFinder:
    def __init__(self):
        self.highest_check = 1
        self.known_primes = []

    def find_primes(self, max_prime, verbose=False):
        # TODO: Only check known primes <= sqrt(check_value)
        start_check = self.highest_check + 1

        for check_value in range(start_check, max_prime + 1):
            is_prime = not check_divisibility(
                check_value, self.known_primes)

            if is_prime:
                self.known_primes.append(check_value)
                if verbose:
                    print(f"Found a prime: {check_value}")

            self.highest_check = check_value
