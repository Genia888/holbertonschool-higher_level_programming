#!/usr/bin/python3
def text_indentation(text):
    """
    This function prints a text with 2 new lines
    after each of these characters: ., ? and :
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    i = 0
    while i < len(text):
        print(text[i], end="")
        if text[i] in ".?:":
            print("\n")
            if i + 1 < len(text) and text[i + 1] == " ":
                i += 1
        i += 1
    print("")
