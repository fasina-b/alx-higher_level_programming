#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4 as hidden
    chars = dir(hidden)
    chars.sort()
    for char in chars:
        if not char.startswith("__"):
            print(char)
