#!/usr/bin/python3
import hidden_4


def hidden_discovery():
    for i in dir(hidden_4):
        if i[:2] != '__':
            print("{:s}".format(i))


if __name__ == '__main__':
    hidden_discovery()
