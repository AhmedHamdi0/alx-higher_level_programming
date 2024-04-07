#!/usr/bin/python3
def uppercase(s):
    for char in s:
        if 97 <= ord(char) <= 122:
            char = chr(ord(char) - 32)
        print(char, end='')
    print()

