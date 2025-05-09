#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    if len(argv) == 1:
        print(f"{len(argv) - 1} arguments.")
    elif len(argv) == 2:
        print(f"{len(argv) - 1} argument:")
    else:
        print(f"{len(argv) - 1} arguments:")
    for i in range(len(argv) - 1):
        print(f"{i + 1}: {argv[i + 1]}")
