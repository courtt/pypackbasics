import argparse

from .other import print_primes

if __name__ == "__main__":
    parser = argparse.ArgumentParser("print_primes")
    parser.add_argument("MAX_PRIME", type=int,
                        help="Print primes <= this value")
    parser.add_argument("--make-plot", action="store_true",
                        help="Make a scatterplot instead of printing")

    args = parser.parse_args()
    print_primes(args.MAX_PRIME, make_plot=args.make_plot)
