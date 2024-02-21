#!/usr/bin/python3
def pow(a, b):
    """Computes a to the power of b and returns the value"""
    result = 1
    for _ in range(abs(b)):
        result *= a
    if b < 0:
        return 1 / result
    return result
