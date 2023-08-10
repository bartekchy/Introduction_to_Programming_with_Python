#!/usr/bin/env python3


def grocery():
    items = []
    grocery_list = {}
    while True:
        try:
            item = input().upper().strip()
            items.append(item)
        except EOFError:
            items.sort()
            last_item = ""
            count = 0
            for item in items:
                if item != last_item:
                    if count == 0:
                        count = 1
                        last_item = item
                        continue
                    else:
                        grocery_list.update({last_item: count})
                        count = 1
                        last_item = item
                        continue
                if item == last_item:
                    count += 1
                    continue
            grocery_list.update({last_item: count})
            break

    for key, value in grocery_list.items():
        print(value, key)


def main():
    grocery()


main()
