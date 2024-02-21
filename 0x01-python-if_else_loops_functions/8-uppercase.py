#!/usr/bin/python3

def uppercase(s):
    """Print a string in uppercase followed by a new line."""
    uppercase_str = ""
    for char in s:
        if ord('a') <= ord(char) <= ord('z'):
            uppercase_str += chr(ord(char) - 32)
        else:
            uppercase_str += char
    print("{}".format(uppercase_str)))
