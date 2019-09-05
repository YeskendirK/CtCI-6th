class Node():
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left, self.right = left, right


# Solution-1a: In-order Traversal with array
index = 0


def tree_to_array(root, arr):
    global index
    if root is None:
        return
    tree_to_array(root.left, arr)
    arr[index] = root.val
    index += 1
    tree_to_array(root.right, arr)


def checkBST_in_order(root):
    arr = [0] * root.size()
    tree_to_array(root, arr)
    for i in range(1, len(arr)):
        if arr[i - 1] <= arr[i]:
            return False
    return True


# Solution-1b; In-Order Traversal without array
last_printed = None


def checkBST_in_order_2(root):
    global last_printed
    if root is None:
        return True
    if not checkBST_in_order_2(root.left):
        return False
    if last_printed is not None and root.val <= last_printed:
        return False
    last_printed = root.val
    if not checkBST_in_order_2(root.right):
        return False

    return True


# Solution-2: Min/Max Solution
def checkBST(root):
    return checkBST_bound(root, None, None)


def checkBST_bound(root, min, max):
    if root is None:
        return True
    if (min is not None and root.val <= min) or (max is not None and root.val > max):
        return False
    if not checkBST_bound(root.left, min, root.val) or not checkBST_bound(root.right, root.val, max):
        return False
    return True


print(checkBST(Node(3, Node(1), Node(8))) is True)
tree1 = Node(5, Node(3, Node(1), Node(4)), Node(7, Node(6), Node(8, None, Node(9))))
print(checkBST(tree1) is True)
tree2 = Node(7, Node(3, Node(1), Node(8)), Node(9, Node(8), Node(11)))
print(checkBST(tree2) is False)
