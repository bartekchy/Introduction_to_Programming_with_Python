#!/usr/bin/env python3

COKE_PRICE = 50
COINS = (5, 10, 25)


def main():
    amount = COKE_PRICE

    while amount > 0:
        print("Amount Due:", amount)
        coin = int(input("Insert Coin: "))

        if coin not in COINS:
            continue

        amount -= coin

    print("Change Owed:", abs(amount))


if __name__ == "__main__":
    main()
