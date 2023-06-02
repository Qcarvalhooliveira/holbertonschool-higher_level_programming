#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    args = len(sys.argv) - 1

    if args == 0:
        print("{} argument.".format(args))
    elif args == 1:
        print("{} argument:".format(args))
    else:
        print("{} arguments:".format(args))
    for i in range(args):
        print("{}: {}".format(i+1, sys.argv[i+1], end=""))
