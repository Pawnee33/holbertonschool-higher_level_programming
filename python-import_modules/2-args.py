#!/usr/bin/python3
import sys
if __name__ == "__main__":
    args_numbers = len(sys.argv) - 1
    if args_numbers == 0:
        print("0 arguments.")
    else:
        token = "argument" if args_numebers == 1 else "arguments"
        print("{} {}: arguments:".format(args_numbers, token))
        for numbers, arg in enumerate(sys.argv[1:], start=1):
            print("{}: {}".format(numbers, arg))
