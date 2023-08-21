#!/usr/bin/env python3

VOWELS = "aeiou"


def twttr(text):
    result = ""

    for t in text:
        if t.lower() not in VOWELS:
            result += t

    return result


def main():
    text = input("input: ")
    print("output: " + twttr(text))


main()
