#!/usr/bin/python3
import sys
args_numbers = len(sys.argv)
print("{} arguments:".format(args_numbers))
for numbers, arg in enumerate(sys.argv[1:], start=1):
    print("{}: {}".format(numbers, arg))
