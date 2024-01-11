def magic_calculation(a, b):
    from magic_calculation_102 import add, sub

    if a < b:
        summed = add(a, b)
        for i in range(4, 6):
            summed = add(summed, i)
        return summed
    else:
        return sub(a, b)
