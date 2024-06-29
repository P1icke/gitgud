# first

import sys
import random

def main():
    try:
        homelander = random.randint(1, 100)
        if homelander == 69:
            print("waltar, delete system32")

        print("This project is now dedicated to solving fizzbuzz")
        while True:
            num = input("Please enter a number to loop from 1 to: ")
            for i in range(1, int(num) + 1):
                if i % 15 == 0:
                    print("fizzbuzz")
                elif i % 3 == 0:
                    print("fizz")
                elif i % 5 == 0:
                    print("buzz")
                else:
                    print(i)
    except:
        print("closed")

if __name__ == "__main__":
    main()