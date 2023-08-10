#!/usr/bin/env python3


def fuel_gauge():
    while True:
        try:
            x = input("Fraction: ").split("/")
            second = int(x.pop())
            first = int(x.pop())
            percent = first / second * 100

            if percent > 100.0:
                continue
            if percent >= 99.0:
                return "F"
            elif percent <= 1.0:
                return "E"
            else:
                return f"{percent:.0f}%"
        except ValueError:
            pass
        except ZeroDivisionError:
            pass


def main():
    print(fuel_gauge())


main()
