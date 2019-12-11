#!/usr/bin/env python3

# Created by : Ben Lapuhapo
# Created on : December 03 2019
# This program uses calculates the running total of a list


def main():
    running_total = []
    while True:
        num = input("Enter the Number of Elements in The List: ")

        print()

        try:
            num_int = int(num)
            for counter in range(0, num_int):
                element = input("Enter Element No." + str(counter+1) + ": ")
                element_int = int(element)
                running_total.append(element_int)
            final_total = [sum(running_total[0:counter+1]) for counter in
                           range(0, len(running_total))]
            print()
            print("The Original Numbers are:{0}".format(running_total))
            print("The Running Total is:{0}".format(final_total))
            break

        except(ValueError):
            print("Not a valid number input")
            print()
            continue

        else:
            break


if __name__ == "__main__":
    main()
