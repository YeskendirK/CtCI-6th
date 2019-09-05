class Node():
    def __init__(self, val=None, left=None, right=None):
        self.val, self.left, self.right = val, left, right


''' Simple Solution '''


def containsTree(t1, t2):
    string1 = get_order_string(t1)
    string2 = get_order_string(t2)
    return string2 in string1


def get_order_string(node):
    sb = ''
    if node is None:
        sb += 'X'
        return sb
    else:
        sb += str(node.val)
        sb += ''
        sb += get_order_string(node.left)
        sb += get_order_string(node.right)
        return sb


tree1 = Node(5, Node(3, Node(2), Node(4)), Node(8, Node(7, Node(9)), Node(1)))
tree2 = Node(8, Node(7), Node(1))

print(containsTree(tree1, tree2) is False)
tree3 = Node(8, Node(7, Node(9)), Node(1))
print(containsTree(tree1, tree3) is True)

''' Alternative Solution '''


def check_subtree(t1, t2):
    if t2 is None:
        return True
    return subtree(t1, t2)


def subtree(t1, t2):
    if t1 is None:
        return False
    elif t1.val == t2.val and match_tree(t1, t2):
        return True
    return subtree(t1.left, t2) or subtree(t1.right, t2)


def match_tree(r1, r2):
    if r1 is None and r2 is None:
        return True
    elif r1 is None or r2 is None:
        return False
    elif r1.val != r2.val:
        return False
    else:
        return match_tree(r1.left, r2.left) and match_tree(r1.right, r2.right)


print(check_subtree(tree1, tree2) is False)
print(check_subtree(tree1, tree3) is True)
