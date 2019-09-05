class Node():
    def __init__(self, item):
        self.right = None
        self.left = None
        self.val = item

    def __str__(self):
        return '(' + str(self.left) + ':L ' + "V:" + str(self.val) + " R:" + str(self.right) + ')'
        # return ' {} :L V: {} R: : {}'.format(str(self.left), str(self.val), str(self.right))


def create_minimal_BST(arr):
    return minimal_BST(arr, 0, len(arr) - 1)


def minimal_BST(arr, start, end):
    if start > end:
        return ''
    mid = (start + end) // 2
    root = Node(arr[mid])
    root.left = minimal_BST(arr, start, mid - 1)
    root.right = minimal_BST(arr, mid + 1, end)
    return root


example = [1, 3, 5, 7, 9, 10, 11]
print(create_minimal_BST(example))
