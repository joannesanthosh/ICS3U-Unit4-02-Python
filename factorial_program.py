#!/usr/bin/env python3

# Created by: Joanne Santhosh
# Created on: Nov 7, 2022


def main():

    loop_counter = 0
    multiply_int = 1

    # This function does the factorial calculation

    # Input
    user_input = input("Enter any positive integer:")
    print("")

    # Process and output
    try:
        integer = int(user_input)
        if integer >= 0:
            while loop_counter < integer:
                loop_counter = loop_counter + 1
                multiply_int = multiply_int * loop_counter
                text = text + " x " + str(loop_counter)
            print("\n{0} = {1}".format(integer, multiply_int))
        elif integer == 0:
            print("\n0 = 0")
        else:
            print("\nError: {} is a negative integer.".format(user_input))
    except ValueError:
        print("\nError: {} is not an integer.".format(user_input))
    finally:
        print("\nDone.")


if __name__ == "__main__":
    main()
