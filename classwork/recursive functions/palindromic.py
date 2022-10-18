def palindromic(lst):
    if len(lst) <= 2:
        return lst[0] == lst[-1]
    if lst[0] != lst[-1]:
        return False
    return palindromic(lst[1:-1])


print(palindromic([1, 2, 3, 4, 5]))
print(palindromic([1, 1, 1, 1, 1]))
print(palindromic([1, 2, 3, 2, 1]))
