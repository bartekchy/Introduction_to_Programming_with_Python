import validators


def validator(email):
    if validators.email(email):
        return "valid"
    else:
        return "Invalid"


def main():
    print(validator(input("What-s tour email address?")))


if __name__ == "__main__":
    main()
