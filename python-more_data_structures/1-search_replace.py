#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = []
    for values in my_list:
        if values == search:
            values = replace
            new_list.append(replace)
        else:
            new_list.append(values)
    return new_list
