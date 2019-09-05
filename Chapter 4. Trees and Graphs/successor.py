class Node():
    def __init__(self, val, left=None, right=None):
        self.val, self.left, self.right = val, left, right
        self.parent = None
        if self.left:
            self.left.parent = self
        if self.right:
            self.right.parent = self


def successor(node):
    if node is None:
        return None
    if node.right is not None:
        return leftMost(node.right)
    else:
        q = node
        x = q.parent
        while x is not None and x.left is not q:
            q = x
            x = x.parent
        return x


def leftMost(node):
    if node is None:
        return None
    while node.left is not None:
        node = node.left
    return node


print(successor(Node(22, Node(11))) is None)
print(successor(Node(22, Node(11), Node(33))).val == 33)
print(successor(Node(22, Node(11), Node(33, Node(28)))).val == 28)
print(successor(Node(22, Node(11), Node(33)).left).val == 22)
print(successor(Node(22, Node(11), Node(33)).right) is None)
