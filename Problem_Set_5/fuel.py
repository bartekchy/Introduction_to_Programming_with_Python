#!/usr/bin/env python3
import sys
import pytest


def convert(fraction):
    fraction = fraction.split("/")
    second = fraction.pop()
    first = fraction.pop()

    if first.isnumeric() and second.isnumeric():
        if second == "0":
            raise ZeroDivisionError
        if second < first:
            raise ValueError
        return int(first) / int(second) * 100
    else:
        raise ValueError


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"


def main():
    print(gauge(convert(input("fuel:"))))


if __name__ == "__main__":
    main()
