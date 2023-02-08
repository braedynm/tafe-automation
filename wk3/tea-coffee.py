# Title: Wk3 Task 1 - Coffee & Tea
# Author: Braedyn Murtagh (braedynm)
# Date: 2023-02-08
#
# Asks the user for their drink preference,
# as well as if they'd like milk and/or sugar.
# If they want sugar, it asks how much they want.
# It then prints out a summary of the request.
#
# Yes, this is ridiculously over-engineered.

# ---------- Main Logic ----------

# Calls to the other functions to ask for input,
# then formats and displays the result.
def main():
    drink = ask_drink()
    m = opt(ask_want("milk"))
    n = opt(ask_sugar(), False)
    s = plural(n)

    print(f"\nAlright. {drink}, {m}milk, {n} sugar{s}. Coming right up.")


# Asks the user if they'd like tea or coffee.
# Valid Responses:
#   [t, tea] -> Tea
#   [c, coffee] -> Coffee
def ask_drink():
    drink = None
    while drink is None:
        choice = clean(input("Would you like tea, or coffee? "))
        if choice in ["t", "tea"]:
            drink = "Tea"
        elif choice in ["c", "coffee"]:
            drink = "Coffee"
        elif len(choice) == 0:
            print("You must choose an option!")
        else:
            print("Invalid Input!")
    return drink


# Asks the user if they want someting.
# Valid Responses:
#   [y, yes] -> True
#   [n, no] -> False
def ask_want(item):
    while True:
        choice = clean(input(f"Would you like {item}? "))
        if choice in ["y", "yes"]:
            return True
        elif choice in ["n", "no"]:
            return False
        elif len(choice) == 0:
            print("You must choose an option!")
        else:
            print("Invalid Input!")


# Asks the user if they want sugar,
# If false, returns false.
# If true, asks how much they want, from 1 to 3.
#   If the user answers 0, returns False.
#   Otherwise, returns the value between 1 to 3.
def ask_sugar():
    if not ask_want("sugar"):
        return False

    while True:
        choice = clean(input("How much sugar do you want (1-3)? "))
        if choice.isnumeric():
            num = int(choice)
            if num in range(1, 4):
                return num
            elif num == 0:
                print("Changed your mind? Alright.")
                return False
            else:
                # Teacher's wording, not mine...
                print("Too much sugar! The doctor says no.")
        else:
            print("Invalid Input!")


# ---------- Utility Functions ----------

# Returns a simplified version of the input string
# in lowercase, without any leading or trailing whitespace.
def clean(s: str):
    return s.lower().strip()


# Formats the input value as an option.
# If the value is false or 0, returns "no" - with an optional trailing space.
# Otherwise, returns an empty string, or the original value if it's a number.
def opt(v, space=True):
    pos = v if type(v) is int else ''
    neg = 'no ' if space is True else 'no'
    return pos if v is not False else neg


# Returns the plural suffix for a value.
# If the value is 1, returns an empty string.
# Otherwise, returns the letter "s"
def plural(n, pos="s", neg=""):
    return pos if type(n) is int and n != 1 else neg


# ---------- Entry ----------

if __name__ == "__main__":
    main()
