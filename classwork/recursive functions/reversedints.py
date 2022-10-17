def reversed_int_list(lst):
    if len(lst) == 1:
        return lst
    return [lst.pop()] + reversed_int_list(lst)


print(reversed_int_list([5, 4, 3, 2, 1]))
print(reversed_int_list([1, 2, 3, 4, 5]))
print(reversed_int_list([1, 2, 3, 4, 5, 6, 7, 8, 9]))
