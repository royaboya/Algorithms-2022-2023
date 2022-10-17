def product_int(lst):
    if len(lst) == 0:
        return 1
    val = lst.pop()
    return val * product_int(lst)


print(product_int([1, 2, 3]))
