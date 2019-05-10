def palindrome(string):
    arr = []
    for c in string:
        c = c.lower()
        if c in arr:
            arr.remove(c)
        else:
            arr.append(c)
    if len(arr) > 1:
        return False
    return True


string = 'bcbAacd'
print(palindrome(string))

# Second solution

''' 
def palindrome(string):
    table = [0 for _ in range(ord('z') - ord('a') + 1)]
    count_odd = 0
    for c in string:
        x = char_number(c)
        if x != -1:
            table[x] += 1
            if table[x] % 2:
                count_odd += 1
            else:
                count_odd -= 1

    return count_odd <= 1
'''
