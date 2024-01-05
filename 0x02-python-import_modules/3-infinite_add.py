#!/usr/bin/python3
import sys
if __name__ == "__main__":
    arg0 = sys.argv[1:]
    ans = sum(map(int, arg0))
    print(ans)
