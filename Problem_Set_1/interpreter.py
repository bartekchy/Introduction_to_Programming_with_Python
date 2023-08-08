#!/usr/bin/env python3


def main():
    (first, sign, second) = input("Expression: ").split(" ")
    first = float(first)
    second = float(second)

    match sign:
        case "+":
            result = first + second
        case "-":
            result = first - second
        case "*":
            result = first * second
        case "/":
            result = first / second

    print(f"{result:.1f}")


main()
