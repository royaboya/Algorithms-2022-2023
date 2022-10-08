def replace_least(lst, num):
    min = lst[0]
    index = 0

    for i in range(len(lst)):
        if lst[i] < min:
            min = lst[i]
            index = i
    lst[index] = num
    return lst

print(replace_least([3, 4], 5), "should be [5, 4].")
print(replace_least([4, 3], 5), "should be [4, 5].")
print(replace_least([4, 4], 5), "should be [5, 4].")
print(replace_least([3, 1, 4, 1, 5, 9], 4), "should be [3, 4, 4, 1, 5, 9].")