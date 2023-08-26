import re
import sys


def convert_hour(hour, min, format):
    result = ""
    if format == "PM":
        hour = int(hour)
        hour += 12
        result += str(hour)
    else:
        result = hour

    if min:
        result += ":"
        result += min
    else:
        result += ":00"
    return result


def convert(s):
    s.strip()
    time = re.search(
        r"(1[0-2]|0?[1-9]):?([0-5][0-9])? (AM|PM) to (1[0-2]|0?[1-9]):?([0-5][0-9])? (AM|PM)",
        s,
    )
    if time:
        result = convert_hour(time.group(1), time.group(2), time.group(3))
        result += " to "
        result += convert_hour(time.group(4), time.group(5), time.group(6))
        return result
    else:
        raise ValueError


def main():
    print(convert(input("Hours: ")))


if __name__ == "__main__":
    main()
