#!/usr/bin/python3
"""
contain the read_file function
"""

def read_file(filename=""):
    """read a text file(UTF8) and prits its to stdout"""
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")
