#!/usr/bin/python3
def no_c(my_string):
    string1 = my_string.translate({ord(i): None for i in 'cC'})
    return string1
