#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):
    try:
        elements = 0
        for i in range(x):
            print(my_list[i], end="")
            elements += 1
    except IndexError:
        pass
    finally:
        print()
        return elements
