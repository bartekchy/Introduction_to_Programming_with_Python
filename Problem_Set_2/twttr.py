#!/usr/bin/env python3

def  twttr(text):

    result=""

    for t in text:
        if t in ('A', 'a', 'E', 'e', 'I', 'i', 'O', 'o', 'U', 'u'):
            continue
        else:
            result += t

    return result

def main():
    
    text = input("input: ")
    print("output: " + twttr(text))
    

main()