#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) >= 1:
        vala0 = tuple_a[0]
    else:
        vala0 = 0
    if len(tuple_a) >= 2:
        vala1 = tuple_a[1]
    else:
        vala1 = 0
    if len(tuple_b) >= 1:
        valb0 = tuple_b[0]
    else:
        valb0 = 0
    if len(tuple_b) >= 2:
        valb1 = tuple_b[1]
    else:
        valb1 = 0
    return vala0 + valb0, vala1 + valb1
