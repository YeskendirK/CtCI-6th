class Node():
    def __init__(self, val=None, left=None, right=None):
        self.val, self.left, self.right = val, left, right


def all_sequences(node):
    result = []
    if node is None:
        return [[]]  # result.append([])
    prefix = []
    prefix.append(node.val)
    left_sequence = all_sequences(node.left)
    right_sequence = all_sequences(node.right)

    for left in left_sequence:
        for right in right_sequence:
            weaved = []
            weave_lists(left, right, weaved, prefix)
            result.extend(weaved)

    return result


def weave_lists(first, second, results, prefix):
    if len(first) == 0 or len(second) == 0:
        result = prefix.copy()
        result.extend(first)
        result.extend(second)
        results.append(result)
        return

    head_first = first.pop(0)
    prefix.append(head_first)
    weave_lists(first, second, results, prefix)
    del prefix[-1]
    first.insert(0, head_first)

    head_second = second.pop(0)
    prefix.append(head_second)
    weave_lists(first, second, results, prefix)
    del prefix[-1]
    second.insert(0, head_second)


import unittest

a = all_sequences(Node(7, Node(4, Node(5)), Node(9)))
print(a)
# Should be
# [[7, 4, 9, 5],
#  [7, 4, 5, 9],
#  [7, 9, 4, 5]]
b = all_sequences(Node(7, Node(4, Node(5), Node(6)), Node(9)))
print(b)

# Should be
# [[7, 4, 9, 5, 6],
#  [7, 4, 9, 6, 5],
#  [7, 4, 5, 9, 6],
#  [7, 4, 5, 6, 9],
#  [7, 4, 6, 9, 5],
#  [7, 4, 6, 5, 9],
#  [7, 9, 4, 5, 6],
#  [7, 9, 4, 6, 5]]
