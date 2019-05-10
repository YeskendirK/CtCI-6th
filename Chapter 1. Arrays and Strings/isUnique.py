def is_unique(s):
    if len(s) > 128:
        return False
    arr = [0] * 128
    for w in s:
        val = ord(w)
        if arr[val] == 1:
            return False
        arr[val] = 1
    return True


print(is_unique('arb'))
