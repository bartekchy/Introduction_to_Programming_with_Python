#!/usr/bin/env python3

def main():
    
    x = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")

    match x.lower():
        case '42' | 'forty-two' | 'forty two':
            print("Yes")
        case _:
            print("No")

main()