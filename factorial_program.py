#!/usr/bin/env python3

# Created by: Joanne Santhosh
# Created on: Nov 7, 2022
# This program uses a while loop


def main():
    # this function finds factorial of a number using while loop

    # input
    int_as_string = input("Enter a positive integer: ")
    print("")

    # variables
    factorial = 1
    loop_counter = 0

    # process & output
    try:
        integer = int(int_as_string)
        if integer >= 0:
            while loop_counter < integer:
                loop_counter = loop_counter + 1
                factorial = factorial * loop_counter
            print("{0}! = {1}.".format(integer, factorial))
        else:
            print("{0}is not a positive integer.".format(integer))
    except ValueError:
        print("{0} is not an integer".format(int_as_string))
    finally:
        print("Done.")


if __name__ == "__main__":
    main()
