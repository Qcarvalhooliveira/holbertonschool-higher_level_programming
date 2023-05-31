#!/usr/bin/python3

for alphabet in range(97, 123):
    if alphabet != 101 and alphabet != 113:
        print("{:c}".format(alphabet), end='')
