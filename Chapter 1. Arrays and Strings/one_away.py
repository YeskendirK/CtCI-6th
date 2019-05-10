def one_away(s, t):
    if len(s) - len(t) > 1:
        return False

    # check replace
    if len(s) == len(t):
        diff = 0
        for i in range(len(s)):
            if s[i] != t[i]:
                diff += 1
        if diff:
            return True
    # check insert
    if len(t) > len(s):
        diff = False
        i = 0
        j = 0
        while i < len(s):

            if s[i] != t[j]:
                if diff:
                    return False
                diff = True
                j += 1
            i += 1
            j += 1
        return True

    # check remove
    if len(s) > len(t):
        diff = False
        i = 0
        j = 0
        while i < len(t):
            if t[i] != s[j]:
                if diff:
                    return False
                diff = True
                j += 1
            i += 1
            j += 1
        return True

    return False


print(one_away('pale', 'ple'))
print(one_away('pale', 'pales'))
print(one_away('pale', 'bale'))
print(one_away('pale', 'bae'))
