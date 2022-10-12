def max_number(lst):
    max = lst[0]
    if len(lst) == 1:
        return 0
    else:
        for i in lst:
            if i > max:
                max = i
    return max


print(max_number([9, 12, 8]))
print(max_number([-2, 1, 0]))
print(max_number([5, 5, 5, 5, 5]))
