def binary_to_string(num):
    if num >= 1 or num <= 0:
        return Exception('ERROR')
    i = 0
    binary = '0.'
    while num > 0:
        if i == 32:
            return Exception('ERROR')
        r = num * 2
        if r >= 1:
            binary += str(1)
            num = r - 1
        else:
            binary += str(0)
            num = r
    return binary


print(binary_to_string(0.72))
