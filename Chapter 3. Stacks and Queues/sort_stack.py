from Stack import Stack


def sort_stack(stack):
    if stack.isEmpty():
        return stack

    out = Stack()

    while not stack.isEmpty():
        temp = stack.pop()
        while not out.isEmpty() and out.peek() > temp:
            stack.push(out.pop())
        out.push(temp)

    return out


arr = [1, 4, 10, 5, 6]
stack = Stack()
for n in arr:
    stack.push(n)
sorted_stack = sort_stack(stack)
out = []
while not sorted_stack.isEmpty():
    x = sorted_stack.pop()
    out.append(x)
print(out)
