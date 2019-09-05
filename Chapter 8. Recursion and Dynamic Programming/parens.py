def add_paren(list, left_rem, right_rem, str):
    if left_rem < 0 or right_rem < 0:
        return

    if left_rem == 0 and right_rem == 0:
        list.append(str)
    else:
        if left_rem > 0:
            add_paren(list, left_rem-1, right_rem, str + '(')

        if right_rem > 0 and right_rem > left_rem:
            add_paren(list, left_rem, right_rem-1, str + ')')

def parens(n):
    if n <= 0:
        return ['']
    else:
        list = []
        add_paren(list, n, n, '')
        return list

print(parens(1))
print(parens(2))
print(parens(3))
