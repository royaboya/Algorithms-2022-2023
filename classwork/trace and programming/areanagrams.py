def are_anagrams(s, t):
    s_dict = {}
    t_dict = {}

    for i in range(len(s)):
        if s[i] not in s_dict:
            s_dict[s[i]] = 0
        s_dict[s[i]] += 1

    for i in range(len(t)):
        if t[i] not in t_dict:
            t_dict[t[i]] = 0
        t_dict[t[i]] += 1

    for i in s:
        if i not in t_dict.keys() or s_dict[i] != t_dict[i]:
            return False
    return True


print(are_anagrams("algorithm", "logarithm"))
print(are_anagrams("test", "tees"))
