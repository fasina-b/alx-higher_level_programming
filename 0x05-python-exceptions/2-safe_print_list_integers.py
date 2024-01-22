def safe_print_list_integers(my_list=[], x=0):
    p_num = 0
    try:
        for i in range(x):
            value = my_list[i]
            if isinstance(value, int):
                print("{:d}".format(value), end="")
                p_num += 1
    except IndexError:
        raise
    finally:
        print()
    return p_num
