def conversion(a, b):
    temp_a, temp_b = a, b
    count = 0
    i = max(temp_a.bit_length(), temp_b.bit_length())
    while i >= 0:
        if temp_a & 1 != temp_b & 1:
            count += 1
        temp_a = temp_a >> 1
        temp_b = temp_b >> 1
        i -= 1

    return count


def conversion2(a, b):
    count = 0
    difference = a ^ b
    while difference != 0:
        count += difference & 1
        difference = difference >> 1
    return count


a = 15
b = 29
print(bin(a))
print(bin(b))
print(conversion2(a, b))