#!/usr/bin/env python3


def main():
    filename = input("File name: ")
    substrings = filename.split(".")

    if len(substrings) == 1:
        print("application/octet-stream")
    else:
        match substrings.pop().lower():
            case "gif":
                print("image/gif")
            case "jpg":
                print("image/jpeg")
            case "jpeg":
                print("image/jpeg")
            case "png":
                print("image/png")
            case "pdf":
                print("application/pdf")
            case "txt":
                print("text/plain")
            case "zip":
                print("application/zip")
            case _:
                print("application/octet-stream")


main()
