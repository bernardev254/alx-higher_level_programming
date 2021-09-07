#!/usr/bin/python3
def uppercase(str):
    for ch in str:
        if ord(ch) >= ord('a') and ord(ch) <= ord('z'):
            char = ch(ord(ch) - 32)
        else:
            char = ch
        print("{:s}".format(char), end="")
    print('')
