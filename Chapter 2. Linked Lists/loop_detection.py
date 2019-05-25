from LinkedList import LinkedList


def loop_detect(linked_list):
    fast = linked_list.head
    slow = linked_list.head

    while fast and fast.nextNode:
        slow = slow.nextNode
        fast = fast.nextNode.nextNode
        if slow == fast:
            break

    if fast is None or fast.nextNode is None:
        return None

    slow = linked_list.head
    while slow != fast:
        slow = slow.nextNode
        fast = fast.nextNode

    return fast
