def compress(s):
    i = 0
    out = ''
    while i < len(s):
        val = s[i]
        c = 1
        while i + c != len(s) and s[i + c] == val:
            c += 1
        out = out + val + str(c)
        i += c

    if len(out) == 2 * len(s):
        return s
    return out


print(compress('aaabbcccd'))
print(compress('abcd'))
