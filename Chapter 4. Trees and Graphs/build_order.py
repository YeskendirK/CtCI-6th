class Queue():
    def __init__(self):
        self.array = []

    def add(self, item):
        self.array.append(item)

    def remove(self):
        return self.array.pop(0)

    def is_empty(self):
        return len(self.array) == 0


class Node():
    def __init__(self, val):
        self.val = val
        self.edges = []
        self.depends_left = 0

    def add_edge(self, node):
        self.edges.append(node)
        node.depends_left += 1


def build_order(projects, depends):
    nodes = {}
    order = []
    for p in projects:
        nodes[p] = Node(p)
    for d in depends:
        nodes[d[0]].add_edge((nodes[d[1]]))
    queue = Queue()
    for p in projects:
        node = nodes[p]
        if not node.depends_left:
            queue.add(node)
    while not queue.is_empty():
        node = queue.remove()
        order.append(node.val)
        for n in node.edges:
            n.depends_left -= 1
            if n.depends_left == 0:
                queue.add(n)
    if len(order) < len(projects):
        return Exception("Cycle Detected!!!")

    return order


projects = ["A", "B", "C", "D", "E", "F", "G"]
dependencies1 = [("C", "A"), ("B", "A"), ("F", "A"), ("F", "B"), ("F", "C"),
                 ("A", "E"), ("B", "E"), ("D", "G")]
print(build_order(projects, dependencies1))  # Should be ["D", "F", "G", "B", "C", "A", "E"]
dependencies2 = [("A", "B"), ("B", "C"), ("C", "D"), ("D", "A")]
print(build_order(projects, dependencies2))  # Should be ''Cycle Detected!!!
dependencies3 = [("A", "B"), ("A", "C"), ("E", "A"), ("E", "B"), ("A", "F"),
                 ("B", "F"), ("C", "F"), ("G", "D")]
print(build_order(projects, dependencies3))  # Should be ["E", "G", "A", "D", "B", "C", "F"]
