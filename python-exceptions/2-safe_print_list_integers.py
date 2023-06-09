#!/usr/bin/python3


def safe_print_list_integers(my_list=[], x=0):
    elements = 0
    try:
        for item in my_list[:x]:
            try:
                if isinstance(item, int):
                    print("{:d}".format(item), end="")
                    elements += 1
            except ValueError:
                pass
    except IndexError:
        pass
    finally:
        print()
        return elements
