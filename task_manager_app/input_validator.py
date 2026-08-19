import re


VALID_PRIORITIES = {"High", "Medium", "Low"}


def validate_string_input(prompt, pattern=None, allow_blank=False):
    while True:
        value = input(prompt).strip()

        if allow_blank and value == "":
            return value

        if not value:
            print("Input cannot be empty.")
            continue

        if pattern and not re.fullmatch(pattern, value):
            print("Invalid input. Please use valid characters.")
            continue

        return value


def validate_priority(prompt="Enter priority (High/Medium/Low): "):
    while True:
        priority = input(prompt).strip().capitalize()

        if priority in VALID_PRIORITIES:
            return priority

        print("Invalid priority. Please enter High, Medium, or Low.")


def validate_numeric_input(prompt):
    while True:
        value = input(prompt).strip()

        try:
            number = int(value)

            if number > 0:
                return number

            print("Please enter a positive number.")

        except ValueError:
            print("Invalid input. Please enter a number.")


def validate_confirmation(prompt):
    while True:
        answer = input(prompt).strip().lower()

        if answer in {"y", "yes"}:
            return True

        if answer in {"n", "no"}:
            return False

        print("Please enter y or n.")
