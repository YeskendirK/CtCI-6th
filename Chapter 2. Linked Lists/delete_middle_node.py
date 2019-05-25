from LinkedList import LinkedList


def delete_middle(node):
    if node is None or node.nextNode is None:
        return False

    next = node.nextNode
    node.data = next.data
    node.nextNode = next.nextNode
    return True


ll = LinkedList()
ll.add_multiple([1, 2, 3, 4])
middle_node = ll.add(5)
ll.add_multiple([7, 8, 9])

print(ll)
delete_middle(middle_node)
print(ll)
