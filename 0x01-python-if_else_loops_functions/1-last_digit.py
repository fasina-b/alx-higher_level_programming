#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
digit_end = abs(number) % 10
message = "Last digit of {} is {} and is ".format(number, digit_end)
if digit_end > 5:
    print(message + "greater than 5")
elif digit_end == 0:
    print(message + "0")
else:
    print(message + "less than 6 and not 0")
