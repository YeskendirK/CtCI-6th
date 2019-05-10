# True = Permutation
# False = NOT Permutation
def check_permutation(s1, s2):
    if len(s1) != len(s2):
        return False
    arr = [0] * 128
    for w in s1:
        arr[ord(w)] += 1
    for w in s2:
        arr[ord(w)] -= 1
        if arr[ord(w)] < 0:
            return False
    return True


s1 = 'abba'
s2 = 'babaa'
print(check_permutation(s1, s2))
