def check_divisibility(value, divisors):
    for divisor in divisors:
        if not value % divisor:
            return True
    return False
