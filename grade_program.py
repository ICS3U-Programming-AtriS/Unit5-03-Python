#!/usr/bin/env python3
# Created By: Atri Sarker
# Date: May 8, 2025
# Program that will take a grade level from the user,
# find out the average mark for that level,
# and display the result to the user.


# Returns the average percentage mark, given the grade level
# According to https://en.wikipedia.org/wiki/Academic_grading_in_Canada#Ontario
def calc_mark(level: str) -> int:
    # Initialize a variable to hold the mark
    mark = 0
    # Match level with mark
    match level:
        case "4+":
            mark = 98
        case "4":
            mark = 91
        case "4-":
            mark = 83
        case "3+":
            mark = 78
        case "3":
            mark = 75
        case "3-":
            mark = 71
        case "2+":
            mark = 68
        case "2":
            mark = 65
        case "2-":
            mark = 61
        case "1+":
            mark = 58
        case "1":
            mark = 55
        case "1-":
            mark = 51
        # DEFAULT CASE [INVALID INPUT]
        case _:
            mark = -1
    # RETURN mark
    return mark


def main():
    # Get user's grade level
    user_level = input("Enter the level that will be converted to a mark percentage: ")
    # Set user's mark percentage
    user_mark = calc_mark(user_level)
    # Check if the user's mark is -1 [INVALID INPUT]
    if user_mark == -1:
        # Tell the user that they entered invalid input
        print(f"{user_level} is not a valid level.")
    else:
        # OTHERWISE, display the user's mark
        print(f"Level {user_level} has a middle percentage of {user_mark}%")


if __name__ == "__main__":
    main()
