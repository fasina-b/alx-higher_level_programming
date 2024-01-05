#!/usr/bin/python3
import hidden_4 as hidden
chars = dir(hidden)
chars.sort()
for char in chars:
    if not char.startswith("__"):
        print(char)
