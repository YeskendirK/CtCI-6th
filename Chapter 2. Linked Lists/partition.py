from LinkedList import LinkedList


def partition(linked_list, x):
    current = linked_list.tail = linked_list.head

    while current:
        nextNode = current.nextNode
        current.nextNode = None
        if current.data < x:
            current.nextNode = linked_list.head
            linked_list.head = current
        else:
            linked_list.tail.nextNode = current
            linked_list.tail = current
        current = nextNode

    linked_list.tail.nextNode = None


example_list = LinkedList()
example_list.generate(10, 0, 9)
print(example_list)
x = 6
partition(example_list, x)
print(example_list)
