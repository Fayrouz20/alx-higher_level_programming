#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    my_bool_list = my_list[:]
    for count, i in enumerate(my_list):
        if i % 2 == 0:
            my_bool_list[count] = True
        else:
            my_bool_list[count] = False
    return(my_bool_list)
