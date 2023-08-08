#!/usr/bin/env python3


def main():
    time = convert(input("What time is it? "))

    if 7.0 <= time <= 8.0:
        print("breakfast time")
    elif 12.0 <= time <= 13.0:
        print("lunch time")
    elif 18.0 <= time <= 19.0:
        print("dinner time")


def convert(time):
    timeEl = time.split(":")

    return float(timeEl[0]) + float(timeEl[1]) / 60


if __name__ == "__main__":
    main()
