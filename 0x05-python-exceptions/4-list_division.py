#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    output = []
    for i in range(list_length):
        try:
            output.append(my_list_1[i] / my_list_2[i])
        except ZeroDivisionError:
            print("division by 0")
            output.append(0)
        except TypeError:
            print("wrong type")
            output.append(0)
        except IndexError:
            print("out of range")
            output.append(0)
        finally:
            pass
    return output
