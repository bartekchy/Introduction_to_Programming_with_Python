#!/usr/bin/env python3


def main():
    x = input("Greeting: ").lower().strip()
    if x.strip().startswith("hello"):
        print("$0")
    elif x.startswith("h"):
        print("$20")
    else:
        print("$100")


main()
