from LinkedList import LinkedList


def level_ll_dfs(root, lists, level):
    if root is None:
        return
    if len(lists) != level:
        list = LinkedList()
        lists.append(list)
    else:
        list = lists[level]
    list.add(root)
    level_ll_dfs(root.left, lists, level + 1)
    level_ll_dfs(root.right, lists, level + 1)


def create_level_ll_dfs(root):
    lists = []
    level_ll_dfs(root, lists, 0)
    return lists


def create_level_ll_bfs(root):
    result = []
    current = LinkedList()
    while len(current) > 0:
        result.append(current)
        parents = current
        current = LinkedList()
        for parent in parents:
            if parent.left is not None:
                current.add(parent.left)
            if parent.right is not None:
                current.add(parent.right)

    return result
