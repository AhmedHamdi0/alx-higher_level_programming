#!/usr/bin/env python3
import sys


def infinite_add():
    args = sys.argv[1:]
    result = sum(int(arg) for arg in args)
    print(result)


if __name__ == "__main__":
    infinite_add()
