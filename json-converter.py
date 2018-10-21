#!usr/bin/env python
"""json-converter.py, by Haakon Gjone, 2018-10-19
This program parse a text file and convert it to a json format
"""

#import json
import random

def main():
    print("Json converter")

    out_of_range = True
    attempts = 4

    while attempts:
        try:
            some_number = int(input("Type in a number between 1 and 100: "))
            print("You typed: " + str(some_number))
            
            if some_number > 100:
                print("Number is too high.")
            elif some_number < 1:
                print("Number is too low.")
            else:
                out_of_range = False
                break

        except:
            print("That's not an integer")
        
        attempts -= 1

        if attempts:
            print("You have " + str(attempts) + " attempts left!")
        else:
            print("No more attempts. Program will exit!")

    if out_of_range == False:       
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
