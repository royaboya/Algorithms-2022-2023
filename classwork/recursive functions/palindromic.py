def palindromic(lst):
    if lst[0] == lst[-1]:
        return True
    return lst[1:] == lst[-2:]


print(palindromic([1, 2, 3, 4, 5]))
print(palindromic([1,1,1,1,1]))
