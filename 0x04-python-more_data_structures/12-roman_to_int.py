#!/bin/usr/python3
def roman_to_int(roman_string):
    if not roman_string or type(roman_string) != str:
        return 0
    dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    number = 0
    for r in range(len(roman_string)):
        if r > 0 and dict[roman_string[r]] > dict[roman_string[r - 1]]:
            number += dict[roman_string[r]] - 2 *\
                    dict[roman_string[r - 1]]
        else:
            number += dict[roman_string[r]]
    return number
