#!/usr/bin/env python3
import inflect

p = inflect.engine()


def main():
    names = []
    while True:
        try:
            names.append(input("Name: "))
        except EOFError:
            print()
            print("Adieu, adieu, to", p.join(names))
            break


if __name__ == "__main__":
    main()
