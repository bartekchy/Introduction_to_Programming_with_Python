#!/usr/bin/env python3

import sys
import csv


def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    students = []
    try:
        with open(sys.argv[1], "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                students.append({"name": row["name"], "house": row["house"]})
    except FileNotFoundError:
        sys.exit(f"Could not read {sys.argv[1]}")

    with open(sys.argv[2], "x") as file:
        writer = csv.DictWriter(file, fieldnames=["first", "last", "house"])
        for student in students:
            name = student["name"].split(",")
            first = name.pop().strip()
            last = name.pop()
            writer.writerow({"first": first, "last": last, "house": student["house"]})


if __name__ == "__main__":
    main()
