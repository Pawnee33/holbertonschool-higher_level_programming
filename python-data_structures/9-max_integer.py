#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list == []:
        return None
    value_m = my_list[0]
    for numbers in my_list:
        if numbers > value_m:
            value_m = numbers
    return value_m
