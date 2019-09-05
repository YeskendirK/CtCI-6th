# import asyncio.queues as Queue
class Queue():
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        return self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)


class Graph():
    def __init__(self):
        self.vertices = []
        self.count = 0

    def add_node(self, node):
        self.vertices.append(node)
        self.count += 1

    def get_nodes(self):
        return self.vertices


class Node():
    def __init__(self, vertex):
        self.vertex = vertex
        self.adjacent = []
        self.adjacentCount = 0
        self.visited = False

    def add_adjacent(self, node):
        self.adjacent.append(node)
        self.adjacentCount += 1

    def get_adjacent(self):
        return self.adjacent

    def get_vertex(self):
        return self.vertex


def bf_search(g, start, end):
    if start == end:
        return True
    q = Queue()
    start.visited = True
    q.enqueue(start)
    while not q.isEmpty():
        u = q.dequeue()
        if u is not None:
            adjacents = u.get_adjacent()
            for node in adjacents:
                if not node.visited:
                    if node == end:
                        return True
                    else:
                        node.visited = True
                        q.enqueue(node)
            u.visited = True

    return False


def create_graph():
    graph = Graph()
    temp = [0] * 6

    temp[0] = Node('a')
    temp[1] = Node('b')
    temp[2] = Node('c')
    temp[3] = Node('d')
    temp[4] = Node('e')
    temp[5] = Node('f')

    temp[0].add_adjacent(temp[1])
    temp[0].add_adjacent(temp[5])
    temp[1].add_adjacent(temp[2])
    temp[1].add_adjacent(temp[4])
    temp[3].add_adjacent(temp[4])
    temp[3].add_adjacent(temp[5])
    temp[4].add_adjacent(temp[2])
    temp[5].add_adjacent(temp[4])

    for i in range(6):
        graph.add_node(temp[i])
    return graph


graph = create_graph()
nodes = graph.get_nodes()
start = nodes[2]
end = nodes[4]
print("Start at: {} End at: ".format(start.get_vertex(), end.get_vertex()))
print(bf_search(graph, start, end))
