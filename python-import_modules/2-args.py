#!/usr/bin/python3
import sys
if __name__ == "__main__":
    args_numbers = len(sys.argv)
    if args_numbers == 1:
        print("{} argument:".format(args_numbers))
    else:
        print("{} arguments:".format(args_numbers))
        for numbers, arg in enumerate(sys.argv[1:], start=1):
            print("{}: {}".format(numbers, arg))
