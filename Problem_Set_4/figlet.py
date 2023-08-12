#!/usr/bin/env python3
import sys
import random
from pyfiglet import Figlet

figlet = Figlet()


def main():
    num_of_arg = len(sys.argv)

    if num_of_arg != 1 and num_of_arg != 3:
        sys.exit("Invalid usage")

    fonts = figlet.getFonts()

    if num_of_arg == 3:
        if sys.argv[1] not in ["-f", "--font"]:
            sys.exit("Invalid usage")
        else:
            try:
                fonts.index(sys.argv[2])
                figlet.setFont(font=sys.argv[2])
            except ValueError:
                sys.exit("Invalid usage")

    if num_of_arg == 1:
        font = random.choice(fonts)
        figlet.setFont(font=font)

    print("Output:", figlet.renderText(input("Input: ")))


if __name__ == "__main__":
    main()
