def URLify(string, n):
    index = len(string)
    string = list(string)
    for i in reversed(range(n)):
        if string[i] == ' ':
            string[index - 3:index] = '%20'
            index -= 3
        else:
            string[index - 1] = string[i]
            index -= 1
    string = ''.join(string)
    return string


arr = 'a b c d      '
print(URLify(arr, 7))
