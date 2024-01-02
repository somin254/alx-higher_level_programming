#!/usr/bin/env python3

def islower(c):
    # Check if the ASCII value of the character is in the lowercase range
    return ord(c) >= ord('a') and ord(c) <= ord('z')

# Example usage
if __name__ == "__main__":
    print("a is {}".format("lower" if islower("a") else "upper"))
    print("H is {}".format("lower" if islower("H") else "upper"))
    print("A is {}".format("lower" if islower("A") else "upper"))
    print("3 is {}".format("lower" if islower("3") else "upper"))
    print("g is {}".format("lower" if islower("g") else "upper"))
