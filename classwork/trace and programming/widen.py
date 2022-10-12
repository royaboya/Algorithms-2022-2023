def widen(s, lst):
    newstr = ""
    if len(s) != len(lst):
        return ""
    for i in range(len(lst)):
        newstr += s[i] * lst[i]
    return newstr


print(widen("cat", [4, 1, 2]))
print(widen("book", [0, 2, 1, 3]))
print(widen("knob", [1, 2, 3]))
print(widen("Hello kitty", [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]))
