#!/usr/bin/python3
def uppercase(s):
    result = ""
    for char in s:
        if 97 <= ord(char) <= 122:
            char = chr(ord(char) - 32)
        result += char
    print("{}".format(result))
