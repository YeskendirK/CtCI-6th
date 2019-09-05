class Node():
    def __init__(self, val=None, left=None, right=None):
        self.val, self.left, self.right = val, left, right
        self.parent = None
        if self.left:
            self.left.parent = self
        if self.right:
            self.right.parent = self


# Solution-1: With Links to Parents
def first_common_ancestor_1(p, q):
    delta = depth(p) - depth(q)
    first = q if delta > 0 else p  # get shallower node
    second = p if delta > 0 else q  # get deeper node
    second = go_up(second, abs(delta))

    while first is not second and first is not None and second is not None:
        first = first.parent
        second = second.parent

    if first is None or second is None:
        return None
    else:
        return first


def depth(node):
    d = 0
    while node is not None:
        node = node.parent
        d += 1
    return d


def go_up(node, delta):
    while delta > 0 and node is not None:
        node = node.parent
        delta -= 1
    return node


# Solution-2: With Links to Parents (Better Worst-Case Solution)
def first_common_ancestor_2(root, p, q):
    if not covers(root, p) or not covers(root, q):
        return None
    elif covers(p, q):
        return p
    elif covers(q, p):
        return q

    sibling = get_sibling(p)
    parent = p.parent()
    while not covers(sibling, q):
        sibling = get_sibling(parent)
        parent = parent.parent


def get_sibling(node):
    if node is None or node.parent is None:
        return None
    parent = node.parent
    if parent.left is node:
        return parent.right
    else:
        return parent.left


def covers(root, p):
    if root is None:
        return False
    if root is p:
        return True
    return covers(root.left, p) or covers(root.right, p)


# Solution-3: Without Links to parents
def first_common_ancestor_3(root, p, q):
    if not covers(root, p) or not covers(root, q):
        return None
    return ancestor_helper(root, q, p)


def ancestor_helper(root, p, q):
    if root is None or root is p or root is q:
        return root
    p_left = covers(root.left, p)
    q_left = covers(root.left, q)
    if p_left != q_left:
        return root

    child_side = root.left if p_left else root.right
    return ancestor_helper(child_side, p, q)


# Test Solution-1
node1 = Node(11, Node(55), Node(77, Node(44)))
node2 = Node(22, Node(99))
print(first_common_ancestor_1(node1, node2))  # None
node3 = Node(33, node1, Node(88, Node(123, None, node2)))
node4 = Node(44, node3, Node(66))
print(first_common_ancestor_1(node1, node2) == node3)  # True
