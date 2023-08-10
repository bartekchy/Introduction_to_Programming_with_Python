#!/usr/bin/env python3

MONTHS = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
]


def change_date():
    while True:
        try:
            date = input("Date: ").split("/")
            if len(date) == 3:
                year = int(date.pop())
                day = int(date.pop())
                month = int(date.pop())
            else:
                date = date.pop().replace(",", "").split(" ")
                year = int(date.pop())
                day = int(date.pop())
                month = MONTHS.index(date.pop()) + 1
            if 1 <= month <= 12 and 1 <= day <= 31 and year >= 0:
                print(f"{year}-{month:02}-{day:02}")
                break
        except ValueError:
            pass


def main():
    change_date()


main()
