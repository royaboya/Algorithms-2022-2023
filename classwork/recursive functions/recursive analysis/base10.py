def base10(digits):
    if len(digits) == 1:
        return digits[0]
    return digits[0] * (10 ** (len(digits) - 1)) + base10(digits[1:])


print(base10([3, 1, 4]))
