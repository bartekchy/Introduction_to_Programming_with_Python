#!/usr/bin/env python3

import requests
import sys
import json


def main():
    if len(sys.argv) != 2:
        sys.exit("Missing command-line argument")
    try:
        bitcoins_to_buy = float(sys.argv[1])
        response = requests.get(
            "https://api.coindesk.com/v1/bpi/currentprice.json"
        ).json()
        price_of_bitcoin = response["bpi"]["USD"]["rate_float"]
        cost = price_of_bitcoin * bitcoins_to_buy
        print(f"${cost:,.4f}")
    except ValueError:
        sys.exit("Command-line argument is not a number")
    except requests.RequestException:
        sys.exit()


if __name__ == "__main__":
    main()
