#!/usr/bin/env python3


def separate(expression):
    result = ""

    for e in expression:
        if e.isupper():
            result += "_" + e.lower()
        else:
            result += e

    return result


def main():
    camel_case = input("camelCase: ")
    print("snake_case:", separate(camel_case))


main()
