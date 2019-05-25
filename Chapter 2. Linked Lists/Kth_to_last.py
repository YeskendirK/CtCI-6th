from LinkedList import LinkedList


def kth_to_last(linked_list, k):
    if linked_list.head is None:
        print('Linked List is empty')
        return 0
    current = linked_list.head
    runner = current
    for i in range(k):
        runner = runner.nextNode
        if runner is None:
            print('Linked List is too short')
            return 0

    while runner:
        runner = runner.nextNode
        current = current.nextNode

    return current.data


def recursive_kth_to_last(ll_head, k):
    if ll_head is None:
        print('Linked List is empty')
        return 0

    index = recursive_kth_to_last(ll_head.nextNode, k) + 1
    if index == k:
        print(' recursive answer: {}'.format(ll_head.data))

    return index


example_list = LinkedList()
example_list.generate(10, 0, 9)
print(example_list)
k = 3
out = kth_to_last(example_list, k)
out_recursive = recursive_kth_to_last(example_list.head, k)
print(out)
print(out_recursive)
