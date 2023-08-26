import re
import sys


def parse(s):
    url = re.search(r"youtube\.com(/embed)?/([^\"]*)", s)

    if url:
        return f"https://youtu.be/{url.group(2)}"
    else:
        return None


def main():
    data = input("HTML: ")
    yt = parse(data)

    if yt:
        print(yt)
    else:
        sys.exit()


if __name__ == "__main__":
    main()
