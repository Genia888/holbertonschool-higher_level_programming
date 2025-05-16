#!/usr/bin/python3
def text_indentation(text):
    """
    Prints a text with 2 new lines after '.', '?', and ':'.
    Removes leading spaces after these punctuation marks.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    delimiters = ".?:"
    start = 0

    for i, char in enumerate(text):
        if char in delimiters:
            print(text[start:i + 1].strip())
            print()
            start = i + 1
            # Skip all following spaces
            while start < len(text) and text[start] == ' ':
                start += 1

    # Print the last part if any
    if start < len(text):
        print(text[start:].strip())
