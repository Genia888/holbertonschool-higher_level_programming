#!/usr/bin/python3
def text_indentation(text):

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    new = ""

    for i in text:
        new += i
        if i in ".:?":
            print("{}".format(new.strip()), end="\n\n")
            new = ""

    if new.strip() != "":
        print("{}".format(new.strip()), end="")
