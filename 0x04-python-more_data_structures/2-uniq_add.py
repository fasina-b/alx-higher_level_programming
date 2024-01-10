#!/usr/bin/python3
def uniq_add(my_list=[]):
    result = 0
    uniqueNum = set()
    for num in my_list:
        if num not in uniqueNum:
            result += num
            uniqueNum.add(num)
    return result
