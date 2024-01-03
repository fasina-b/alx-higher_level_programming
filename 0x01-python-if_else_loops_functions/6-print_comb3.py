#!/usr/bin/python3
num1 = 0
while num1 <= 89:
    if num1 % 10 == 0:
        num1 += 1 + num1 // 10
    print("{:02d}".format(num1), end='\n' if num1 == 89 else ", ")
    num1 += 1
