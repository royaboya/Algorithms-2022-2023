def palindromic(lst):
    if len(lst) <= 2:
        print(lst)
        return lst[0] == lst[-1]
    if lst[0] != lst[-1]:
        print(lst)
        return False
    return palindromic(lst[1:-1])


print(palindromic([1, 2, 3, 4, 5]))
print(palindromic([1, 1, 1, 1, 1]))
print(palindromic([1, 2, 3, 2, 1]))
