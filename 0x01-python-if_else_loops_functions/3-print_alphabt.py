#!/usr/bin/python3
for alphas in range(97, 123):
    if chr(alphas) not in 'qe':
        print("{}".format(chr(alphas)), end="")
