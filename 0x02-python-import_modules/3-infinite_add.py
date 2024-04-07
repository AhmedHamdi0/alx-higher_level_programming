#!/usr/bin/python3
import sys


def infinite_add():
    num_args = len(sys.argv[1:])
    if num_args == 0:
        print('{:d}'.format(0))
    else:
        int_argument = [int(arg) for arg in sys.argv[1:]]
        result = 0
        for i in range(0, num_args):
            result += int_argument[i]
        print(result)


if __name__ == "__main__":
    infinite_add()
