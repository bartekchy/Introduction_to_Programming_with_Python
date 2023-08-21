#!/usr/bin/env python3

import sys
import os
from PIL import Image
from PIL import ImageOps


def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    first = os.path.splitext(sys.argv[1])
    second = os.path.splitext(sys.argv[2])
    first_suffix = first[-1]
    second_suffix = second[-1]

    if first_suffix.lower() and second_suffix.lower() not in (".jpg", ".png", ".jpeg"):
        sys.exit("Invalid input")

    if first_suffix != second_suffix:
        sys.exit("Input and output have different extensions")

    try:
        shirt = Image.open("shirt.png")
        size = shirt.size

        muppet = Image.open(sys.argv[1])
        muppet = ImageOps.fit(muppet, size)

        muppet.paste(shirt, (0, 0), mask=shirt)

        muppet.save(sys.argv[2])

    except FileNotFoundError:
        sys.exit("Input does not exist")


if __name__ == "__main__":
    main()
