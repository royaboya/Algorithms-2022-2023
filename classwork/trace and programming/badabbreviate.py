def bad_abbreviate(s):
    newstr = ""

    for i in range(0, len(s), 2):
        newstr += s[i]

    return newstr


print(bad_abbreviate("second"))
print(bad_abbreviate("They called me Mr. Glass."))
