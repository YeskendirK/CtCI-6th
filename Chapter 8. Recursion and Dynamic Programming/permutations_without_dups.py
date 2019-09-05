# Solution-1

def get_perms(str):
    if str is None:
        return None
    permutations = []
    if len(str) == 0:
        permutations.append('')
        return permutations

    first = str[0]
    remainder = str[1:]
    words = get_perms(remainder)
    for w in words:
        for i in range(len(w) + 1):
            s = w[:i] + first + w[i:]
            permutations.append(s)

    return permutations


# Solution-2

def get_perms2(str):
    result = []
    length = len(str)
    if length == 0:
        result.append('')
        return result

    for i in range(0, length):
        partials = get_perms2(str[:i] + str[i + 1:])

        for s in partials:
            result.append(str[i] + s)
    return result


s = 'ABC'
print(get_perms(s))
print(get_perms2(s))
