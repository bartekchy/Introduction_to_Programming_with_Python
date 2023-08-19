#!/usr/bin/env python3

VOWELS = "aeiou"


def shorten(word):
    result = ""

    for t in word:
        if t.lower() not in VOWELS:
            result += t

    return result


def main():
    text = input("input: ")
    print("output: " + shorten(text))


if __name__ == "__main__":
    main()
