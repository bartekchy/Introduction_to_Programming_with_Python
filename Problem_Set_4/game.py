#!/usr/bin/env python3
import random


def game():
    while True:
        try:
            level = int(input("Level: "))
            if level <= 0:
                continue
            else:
                lucku_number = random.randint(1, level + 1)
                while True:
                    try:
                        guess = int(input("Guess: "))
                        if 0 >= guess:
                            continue

                        if guess < lucku_number:
                            print("Too small!")
                        elif guess > lucku_number:
                            print("Too large!")
                        else:
                            print("Just right!")
                            break
                    except ValueError:
                        pass
                break

        except ValueError:
            pass

    return


def main():
    game()


if __name__ == "__main__":
    main()
