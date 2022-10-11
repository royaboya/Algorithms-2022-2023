def count_spaces(s):
    """Returns the number of space characters in s.

    s - string"""
    c = 0

    for i in s:
        if  i == ' ':
            c+=1

    return c

#Test cases
print(count_spaces("spaces"), "is 0")
print(count_spaces("hi there"), "is 1")
print(count_spaces("Y M C A"), "is 3")



