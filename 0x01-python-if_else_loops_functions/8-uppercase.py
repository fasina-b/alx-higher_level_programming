#!/usr/bin/python3
def uppercase(input_str):
    for alphas in input_str:
        print("{}".format(chr(ord(alphas) - 32) if ord(alphas) >= 97 and ord(alphas) <= 122 else alphas), end="")
    print()
