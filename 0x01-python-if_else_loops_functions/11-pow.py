#!/usr/bin/env python3

def pow(a, b):
    # Calculate the power of a to the b
    result = a ** b
    
    # Return the result
    return result

# Example usage
if __name__ == "__main__":
    print(pow(2, 2))
    print(pow(98, 2))
    print(pow(98, 0))
    print(pow(100, -2))
    print(pow(-4, 5))
