import random


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if 1 <= level <= 3:
                return level
        except ValueError:
            pass


def generate_integer(level):
    if level in (1, 2, 3):
        return random.randint(1, 9**level)


def professor(level):
    score = 0
    for i in range(10):
        first_num = generate_integer(level)
        second_num = generate_integer(level)
        perf = 0
        while True:
            try:
                result = int(input(f"{first_num} + {second_num} = "))
                if result == first_num + second_num:
                    score += 1
                    break
                else:
                    print("EEE")
                    perf += 1
                    if perf == 3:
                        break
                    continue
            except ValueError:
                perf += 1
                if perf == 3:
                    break
                pass
        print("loop")
    print("Score:", score)


def main():
    level = get_level()
    professor(level)


if __name__ == "__main__":
    main()
