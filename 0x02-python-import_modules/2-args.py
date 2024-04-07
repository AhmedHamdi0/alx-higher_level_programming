#!/usr/bin/python3
import sys


def print_arguments():
    args = sys.argv[1:]
    num_args = len(args)
    if num_args == 0:
        print('{} arguments.'.format(0))
        return

    print("{} argument{}".format(num_args, 's:' if num_args != 1 else ':'))

    for i, arg in enumerate(args, start=1):
        print("{}: {}".format(i, arg))


if __name__ == "__main__":
    print_arguments()
