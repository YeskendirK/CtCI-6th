def do(arr):
    arr.sort()
    new_arr = [0] * len(arr)
    low = 0
    high = len(arr) - 1
    begin = False
    current = 0
    while high >= low:
        if begin:
            new_arr[current] = arr[low]
            low += 1
            begin = False
        else:
            new_arr[current] = arr[high]
            high -= 1
            begin = True
        current += 1

    return new_arr

def sort_valley_peak(arr):
    i = 1
    while i < len(arr):
        biggest_idx = max_index(arr, i-1, i, i+1)
        if i != biggest_idx:
            swap(arr, i, biggest_idx)
        i += 2

def max_index(arr, a, b, c):
    a_val = arr[a] if 0 <= a < len(arr) else float('-inf')
    b_val = arr[b] if 0 <= b < len(arr) else float('-inf')
    c_val = arr[c] if 0 <= c < len(arr) else float('-inf')

    max_num = max(a_val, b_val, c_val)
    if a_val == max_num:
        return a
    elif b_val == max_num:
        return b
    else:
        return c

def swap(arr, left, right):
    temp = arr[left]
    arr[left] = arr[right]
    arr[right] = temp

a = [9,1,0,4,8,7]
sort_valley_peak(a)
print(a)
