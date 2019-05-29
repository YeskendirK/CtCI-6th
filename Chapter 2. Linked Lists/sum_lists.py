from LinkedList import LinkedList, Node


# Solution 1
def sum_lists(first, second):
    out_list = LinkedList()
    out_list.head = out_list.tail = None
    out = find_int(first) + find_int(second)
    while out > 0:
        num = out % 10
        out /= 10
        out_list.add(num)

    return out_list


def find_int(l):
    if l.head is None:
        return 0
    current = l.head
    out, dec = 0, 1
    while current:
        out += current.data * dec
        current = current.nextNode
        dec *= 10
    return out


# Soulution 1 FOLLOWUP
def sum_lists_followup(first, second):
    out_list = LinkedList()
    out_list.head = out_list.tail = None
    out = find_int_followup(first) + find_int_followup(second)
    for c in str(out):
        out_list.add(int(c))
    return out_list


def find_int_followup(l):
    if l.head is None:
        return 0
    current = l.head
    out_str = ''
    while current:
        out_str += str(current.data)
        current = current.nextNode
    return int(out_str)


# Soultion 3
def addLists(list1, list2):
    node1, node2 = list1.head, list2.head
    out_list = LinkedList()
    carry = 0
    while node1 or node2:
        result = carry
        if node1:
            result += node1.data
            node1 = node1.nextNode
        if node2:
            result += node2.data
            node2 = node2.nextNode
        out_list.add(result % 10)
        carry = result // 10

    if carry:
        out_list.add(carry)

    return out_list


example_one = LinkedList()
example_two = LinkedList()
example_one.generate(3, 0, 9)
example_two.generate(3, 0, 9)
print(example_one)
print(example_two)
print('Solution 1')
print(sum_lists(example_one, example_two))
print('Solution 1 FOLLOWUP')
print(sum_lists_followup(example_one, example_two))
print('Solution 3')
print(addLists(example_one, example_two))
