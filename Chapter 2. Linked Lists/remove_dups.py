from LinkedList import LinkedList


def remove_dups(linked_list):
    if linked_list.head is None:
        return linked_list
    else:

        current = linked_list.head
        visited = set([current.data])
        while current.nextNode:
            if current.nextNode.data in visited:
                current.nextNode = current.nextNode.nextNode
            else:
                visited.add(current.nextNode.data)
                current = current.nextNode
    return linked_list


def remove_dups_followup(linked_list):
    if linked_list.head is None:
        return linked_list
    else:
        current = linked_list.head
        while current:
            runner = current
            while runner.nextNode:
                if runner.nextNode.data == current.data:
                    runner.nextNode = runner.nextNode.nextNode
                else:
                    runner = runner.nextNode
            current = current.nextNode
    return linked_list


example_list = LinkedList()
example_list.generate(50, 0, 9)
print(example_list)
remove_dups(example_list)
print(example_list)
