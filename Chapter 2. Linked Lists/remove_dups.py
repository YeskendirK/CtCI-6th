from LinkedList import LinkedList


def remove_dups(linked_list):
    if linked_list.head is None:
        return linked_list
    else:
        visited = set()
        current = linked_list.head
        while current.nextNode:
            if current.nextNode.data in visited:
                current.nextNode = current.nextNode.nextNode
            else:
                visited.add(current.nextNode.data)
                current = current.nextNode
    return linked_list


example_list = LinkedList()
example_list.generate(50, 0, 9)
print(example_list)
remove_dups(example_list)
print(example_list)
