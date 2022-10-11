def count_vowels(s):
    """Returns the number of vowels in s.

    s - string"""

    vowels = "aeiou"
    c = 0
    for i in s:
        if i.lower() in vowels:
            c += 1

    return c


# Test cases
print(count_vowels("spaces"), "is 2")
print(count_vowels("hi there"), "is 3")
print(count_vowels("Y M C A"), "is 1")
