import re
import sys


def validate(ip):
    tmp = ip.split(".")

    if len(tmp) != 4:
        return False

    for t in tmp:
        if t.isnumeric():
            if 0 <= int(t) <= 255:
                continue
            else:
                return False
        else:
            return False

    return True


def main():
    print(validate(input("IPv4 Address: ")))


if __name__ == "__main__":
    main()
