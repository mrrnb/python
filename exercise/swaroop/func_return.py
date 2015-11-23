#!/usr/bin/python
# Filename: func_return.py

def func(x,y):
    '''Print the maximum of two numbers.

    The two values must be integers.'''
    if x>y:
        return x
    else:
        return y
print func(1,2)
print func.__doc__
help(func)
