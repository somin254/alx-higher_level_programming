#!/usr/bin/env python3

def fizzbuzz():
    # Loop through numbers from 1 to 100
    for i in range(1, 101):
        # Check for multiples of both three and five
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz", end=' ')
        # Check for multiples of three
        elif i % 3 == 0:
            print("Fizz", end=' ')
        # Check for multiples of five
        elif i % 5 == 0:
            print("Buzz", end=' ')
        # Print the number itself
        else:
            print(i, end=' ')

# Example usage
if __name__ == "__main__":
    fizzbuzz()
