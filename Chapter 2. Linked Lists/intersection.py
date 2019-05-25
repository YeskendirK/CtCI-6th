from LinkedList import LinkedList


def intersection(first, second):
    node1, node2 = first.head, second.head
    diff = abs(len(first) - len(second))
    inter_node = None
    if len(first) > len(second):
        for i in range(diff):
            node1 = node1.nextNode
    elif len(second) > len(first):
        for i in range(diff):
            node2 = node2.nextNode
    while node1 and node2:
        if node1 == node2:
            inter_node = node1
            break
        node1 = node1.nextNode
        node2 = node2.nextNode
    return inter_node
