#!usr/bin/env python
"""json-converter.py, by Haakon Gjone, 2018-10-19
This program parse a text file and convert it to a json format
"""

#import json
import random

def read_input():
    attempts = 4
    attempt_text = [" attempt", " attempts"]

    while attempts:
        try:
            input_number = int(input("Type in a number between 1 and 100: "))
            print("You typed: " + str(input_number))
            
            if input_number > 100:
                print("Number is too high.")
            elif input_number < 1:
                print("Number is too low.")
            else:
                break

        except:
            print("That's not an integer")

        attempts -= 1
        
        if attempts:
            index = 1
            
            if attempts == 1:
                index = 0

            print("You have " + str(attempts) + attempt_text[index] + " left!")
        else:
            input_number = -1
            print("No more attempts. Program will exit!")

    return input_number

def main():
    print("Json converter")

    some_number = read_input()
    if some_number > 0:
        line_number = 1
        random_numbers = []

        while(some_number):
            random_number = random.randint(1,100)
            random_numbers.append(random_number)
            print(str(line_number) + "*" * random_number + " " + str(random_number))
            some_number -= 1
            line_number += 1

        print(random_numbers)
        print(sorted(random_numbers))
        print("Size of list: " + str(len(random_numbers)))

if __name__ == "__main__":
    main()
