#!/usr/bin/env python3

import sys
import csv
from tabulate import tabulate


def main():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

    try:
        filename = sys.argv[1]
        substrings = filename.split(".")
        suffix = substrings.pop()
        if suffix != "csv":
            sys.exit("Not a CSV file")

        menu = []

        with open(sys.argv[1]) as file:
            reader = csv.reader(file)
            for first, second, third in reader:
                menu.append({"first": first, "second": second, "third": third})
        print(tabulate(menu, headers="firstrow", tablefmt="grid"))

    except FileNotFoundError:
        sys.exit("File does not exist")


if __name__ == "__main__":
    main()
