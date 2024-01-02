#!/usr/bin/env python3

def uppercase(str):
    # Loop through each character in the string
    for c in str:
        # Check if the character is lowercase using ASCII values
        if ord(c) >= ord('a') and ord(c) <= ord('z'):
            # Print the uppercase version of the character without a newline
            print(chr(ord(c) - ord('a') + ord('A')), end="")
        else:
            # Print the character without a newline
            print(c, end="")
    
    # Print a newline after the loop
    print()

# Example usage
if __name__ == "__main__":
    uppercase("best")
    uppercase("Best School 98 Battery street")
