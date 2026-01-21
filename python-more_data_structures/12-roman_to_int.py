#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str):
        return 0
    roman_dic = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }
    total = 0
    for index in range(len(roman_string) - 1):
        actual_value = roman_dic[roman_string[index]]
        next_value = roman_dic[roman_string[index + 1]]
        if actual_value < next_value:
            total -= actual_value
        else:
            total += actual_value
    total += roman_dic[roman_string[-1]]
    return total
