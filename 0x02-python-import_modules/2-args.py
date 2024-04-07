#!/usr/bin/python3
import sys

if __name__ == "__main__":
    args = sys.argv[1:]
    num_args = len(args)

    print("{:d} argument{:s}:".format(num_args, 's' if num_args != 1 else ''))

    if num_args > 0:
        for i, arg in enumerate(args, start=1):
            print("{:d}: {:s}".format(i, arg))
    else:
        print("No arguments.")
