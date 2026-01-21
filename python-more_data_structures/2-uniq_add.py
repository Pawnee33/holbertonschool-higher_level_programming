#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique = []
    for numbers in my_list:
        if numbers not in unique:
            unique.append(numbers)
    return sum(unique)
