#!/usr/bin/env python3

def main():
    
    expresion = input("Expression: ")
    expresionEl = expresion.split(" ")

    match expresionEl[1]:
        case '+':
            sum = float(expresionEl[0]) + float(expresionEl[2])
            print(f"{sum:.1f}")
        case '-':
            diff = float(expresionEl[0]) - float(expresionEl[2])
            print(f"{diff:.1f}")
        case '*':
            prod = float(expresionEl[0]) * float(expresionEl[2])
            print(f"{prod:.1f}")
        case '/':
            quot = float(expresionEl[0]) / float(expresionEl[2])
            print(f"{quot:.1f}")
            
main()