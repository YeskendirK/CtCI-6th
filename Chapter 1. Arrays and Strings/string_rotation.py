def isSubstring(string, sub):
    return string.find(sub) != -1


def isRotation(s1, s2):
    if len(s1) == len(s2) != 0:
        return isSubstring(s1 + s1, s2)
    return False
