#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4

    names = dir(hidden_4)
    for each_name in names:
        if not each_name.startswith("__"):
            print("{}".format(each_name))
