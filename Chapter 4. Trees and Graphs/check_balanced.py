def get_height(root):
    if root is None:
        return -1
    return max(get_height(root.left), get_height(root.right)) + 1


def check_balanced(root):
    if root is None:
        return True
    diff = get_height(root.lef) - get_height(root.right)
    if abs(diff) > 1:
        return False
    else:
        check_balanced(root.left) and check_balanced(root.right)


def check_height(root):
    if root is None:
        return -1
    left_h = check_height(root.left)
    if left_h == -10: return left_h

    right_h = check_height(root.right)
    if right_h == -10: return right_h

    diff = left_h - right_h
    if abs(diff) > 1:
        return -10
    else:
        return max(left_h, right_h) + 1


def is_balanced(root):
    return check_height(root) != -10
