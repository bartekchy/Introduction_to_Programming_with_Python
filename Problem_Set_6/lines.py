#!/usr/bin/env python3

import sys


def main():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    print(sys.argv[1])
    try:
        filename = sys.argv[1]
        substrings = filename.split(".")
        suffix = substrings.pop()
        if suffix != "py":
            sys.exit("Not a python file")

        count = 0
        with open(sys.argv[1], "r") as file:
            lines = file.readlines()

        for line in lines:
            line = line.lstrip()
            if line.startswith("#") or line == "":
                continue
            count += 1

        print(count)

    except FileNotFoundError:
        sys.exit("File does not exist")


if __name__ == "__main__":
    main()
