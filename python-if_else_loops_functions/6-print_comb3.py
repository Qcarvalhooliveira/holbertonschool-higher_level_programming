#!/usr/bin/python3

for digit_one in range(0, 10):
    for digit_two in range(digit_one + 1, 10):
        if digit_one == 8 and digit_two == 9:
            print("{}{}".format(digit_one, digit_two))
        else:
            print("{}{}".format(digit_one, digit_two), end=", ")
