#!/usr/bin/python3
import hidden_4 as hidden
if __name__ == "__main__":
    chars = dir(hidden)
    chars.sort()
    for char in chars:
        if not char.startswith("__"):
            print(char)
