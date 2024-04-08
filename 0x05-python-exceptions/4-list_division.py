#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result_list = []
    try:
        for i in range(list_length):
            try:
                div_result = float(my_list_1[i]) / float(my_list_2[i])
            except ZeroDivisionError:
                result_list.append(0)
                print("division by 0")
            except ValueError:  
                result_list.append(0)
                print("wrong type")
            except IndexError:
                print("out of range")
                break
            else:
                result_list.append(div_result)
    finally:
        return result_list
