# Solution-1: Recursion

def get_subset(sets, i):
    all_subsets = []
    if len(sets) == i:
        if [] not in all_subsets:
            all_subsets.append([])
    else:
        all_subsets = get_subset(sets, i + 1)
        more_subsets = []
        item = sets[i]
        for subset in all_subsets:
            new_subset = []
            [new_subset.append(value) for value in subset]
            new_subset.append(item)
            more_subsets.append(new_subset)
        [all_subsets.append(value) for value in more_subsets]
    return all_subsets


# Solution-2: Combinatorics

def get_subset2(set):
    all_subsets = []
    max = 1 << len(set)
    for k in range(max):
        subset = convert_to_set(k, set)
        all_subsets.append(subset)

    return all_subsets


def convert_to_set(k, set):
    subset = []
    index = 0
    while k > 0:
        if k & 1 == 1 and set[index] not in subset:
            subset.append(set[index])
        index += 1
        k >>= 1
    return subset



s = ['a', 'b', 'c']
print(get_subset(s, 0))
print(get_subset2(s))