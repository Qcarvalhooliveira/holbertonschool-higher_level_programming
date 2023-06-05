#!/usr/bin/env python3
def no_c(my_string):
    my_string = ''.join(i for i in my_string if i != 'c' and i != 'C')
    return (my_string)
