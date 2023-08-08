#!/usr/bin/env python3


def coke():
    cost = 50

    while True:
        print("Amount Due:" + str(cost))
        coin = int(input("Insert Due: "))

        if coin in (5, 10, 25):
            cost -= coin

            if cost <= 0:
                print("change Owed: " + str(cost * -1))
                break

            else:
                print("change Owed: 0")
                continue

        else:
            continue


def main():
    coke()


main()
