#!/usr/bin/python3


def text_indentation(text):
    """
        Prints a new line

        Raise:
            TypeError: text must be a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    new_text = ""
    for string in text:
        new_text += string
        if string in [".", "?", ":"]:
            new_text += "\n\n"

    print(new_text)


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/5-text_indentation.txt")
