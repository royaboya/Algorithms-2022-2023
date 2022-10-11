from tkinter import E


def l33tify(s):
    """Returns s with 3 replacing e/E.

    s - string"""

    new_string = ""

    for i in s:
        if i.lower() != "e":
            new_string += i
        else:
            new_string += "3"

    return new_string


# Test cases
print(l33tify("spaces"), "is spac3s")
print(l33tify("hi there"), "is hi th3r3")
print(l33tify("Y M C A"), "is Y M C A")
