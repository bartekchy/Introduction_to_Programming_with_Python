from datetime import date
import sys
import inflect

P = inflect.engine()


def minutes_from_birth(birth_date_str):
    try:
        birth_date = date.fromisoformat(birth_date_str)
        todays_date = date.today()
        timedelta = todays_date - birth_date
        minutes = int(timedelta.total_seconds() / 60)
        return f"{P.number_to_words(minutes)} minutes"
    except ValueError:
        sys.exit("Invalid date")


def main():
    print(minutes_from_birth(input("Date of Birth:")))


if __name__ == "__main__":
    main()
