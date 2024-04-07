#!/usr/bin/env python3
import sys


def infinite_add():
    args = sys.argv[1:]
    total = sum(map(int, args))
    print(total, end='\n')


if __name__ == "__main__":
    infinite_add()
