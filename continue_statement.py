#!/usr/bin/env python3

# Created by: Huzaifa Khalid
# Created on: April 2022
# This program calculates sum of only positive integers


import random


def main():
    # this function uses a for loop
    counter = 0
    total = 0

    # input
    user_number_as_string = input("How many number(s) are you going to add: ")
    print("")

    # process & output
    try:
        user_number_as_integer = int(user_number_as_string)
        for counter in range(user_number_as_integer):
            counter = counter + 1
            second_input_str = input("Enter your number(s): ")
            print("")
            second_input_int = int(second_input_str)
            if second_input_int < 0:
                continue
            total = total + second_input_int

        print("The sum of positive numbers is = {0}".format(total))

    except Exception:
        print("invalid input, enter a integer you dope.")

    print("\nDone.")


if __name__ == "__main__":
    main()
