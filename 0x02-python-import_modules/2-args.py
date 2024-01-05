#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argc = len(sys.argv) - 1
    opp = "argument" if argc == 1 else "arguments"
    char = ":" if argc else "."
    print("{} {}{}".format(argc, opp, char))
    for i in range(1, argc + 1):
        print("{}: {}".format(i, sys.argv[i]))
