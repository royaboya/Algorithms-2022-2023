def exp(num):
    if num == 0:
        return 1
    return 10 * exp(num - 1)


print(exp(5))
print(exp(4))
print(exp(3))
print(exp(2))
