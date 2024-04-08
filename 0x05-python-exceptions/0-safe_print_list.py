#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    printed_elements = 0
    try:
        for element in my_list[:x]:
            print(element, end='')
            printed_elements += 1
    except IndexError:
        pass
    print()
    return printed_elements
