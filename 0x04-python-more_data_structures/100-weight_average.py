#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    weighted = 0
    total_weight = 0
    for tup in my_list:
        weighted += tup[0] * tup[1]
        total_weight += tup[1]
    return weighted / total_weight
