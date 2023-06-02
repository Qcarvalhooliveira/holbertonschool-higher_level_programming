#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    args = len(sys.argv) - 1

    if args <= 1:
        print("{} Argument.".format(args))
    else:
        print("{} Arguments:".format(args))
    for i in range(args):
        print("{}: {}".format(i+1, sys.argv[i+1], end=""))
