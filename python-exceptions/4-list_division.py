#!/usr/bin/python3
def list_division(my_l_1, my_l_2, list_length):
    result = []
    for index in range(list_length):
        try:
            new_list = my_l_1[index] / my_l_2[index]
        except TypeError:
            new_list = 0
            print("wrong type")
        except ZeroDivisionError:
            new_list = 0
            print("division by 0")
        except IndexError:
            new_list = 0
            print("out of range")
        finally:
            result.append(new_list)
    return result
