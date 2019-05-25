from LinkedList import LinkedList


def palindrome(linked_list):
    if linked_list.head is None:
        return False

    if linked_list.head == linked_list.tail:
        return True

    if linked_list.head.data is not linked_list.tail.data:
        return False
    elif linked_list.head.nextNode is linked_list.tail:
       return True
    else:
        prev_last = linked_list.head
        while prev_last.nextNode.nextNode:
            prev_last = prev_last.nextNode
        linked_list.head = linked_list.head.nextNode
        prev_last.nextNode = None
        linked_list.tail = prev_last
        return palindrome(linked_list)


example = '1'
example_list = LinkedList()
for c in example:
    example_list.add(int(c))
print(example_list)
print(palindrome(example_list))
