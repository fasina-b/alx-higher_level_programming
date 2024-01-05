#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    arg0 = sys.argv[1:]
    ans = sum(map(int, arg0))
    print(ans)
