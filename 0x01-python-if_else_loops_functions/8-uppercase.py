#!/usr/bin/python3

def uppercase(s):
    """Print a string in uppercase followed by a new line."""
    for char in s:
        if ord('a') <= ord(char) <= ord('z'):
            print("{:c}".format(ord(char) - 32), end="")
        else:
            print("{:c}".format(ord(char)), end="")
    print()
