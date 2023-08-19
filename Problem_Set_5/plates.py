#!/usr/bin/env python3


def is_valid(s):
    if is_string_not_have_correct_form_and_len(s):
        return False

    if is_string_start_with_numbers(s):
        return False

    if is_str_ends_with_numbers(s):
        return True

    else:
        return False


def is_string_not_have_correct_form_and_len(s):
    if s.isalnum() and 2 <= len(s) <= 6:
        return False

    else:
        return True


def is_string_start_with_numbers(s):
    prefix = ""

    for c in s[:2]:
        prefix += c

    return any(char.isdigit() for char in prefix)


def is_str_ends_with_numbers(s):
    is_str_have_number = 0

    for c in s:
        if c == "0" and is_str_have_number == 0:
            return False

        if c.isnumeric():
            is_str_have_number = 1

        if c.isalpha() and is_str_have_number == 1:
            return False

    return True


def main():
    plate = input("Plate: ")

    if is_valid(plate):
        print("Valid")

    else:
        print("Invalid")


if __name__ == "__main__":
    main()
