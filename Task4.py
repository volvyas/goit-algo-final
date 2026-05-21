import uuid
import heapq as hq

import networkx as nx
import matplotlib.pyplot as plt


class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color	# Додатковий аргумент для зберігання кольору вузла
        self.id = str(uuid.uuid4())	# Унікальний ідентифікатор для кожного вузла

    def __lt__(self, other):
        return self.val > other.val #TODO implemented max heap. reverse sign to make min

class Heap:
    def __init__(self):
        self._nodes = []

    def get_root(self):
        if len(self._nodes) == 0:
            return None

        for i, node in enumerate(self._nodes):
            left_index = 2 * i + 1
            right_index = 2 * i + 2

            if left_index < len(self._nodes):
                node.left = self._nodes[left_index]
            if right_index < len(self._nodes):
                node.right = self._nodes[right_index]

        return self._nodes[0]

    def add_node(self, node):
        hq.heappush(self._nodes, node)


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)	# Використання id та збереження значення вузла
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph


def draw_heap(heap_graph):
    heap_graph = nx.DiGraph()
    heap_root = heap.get_root()
    pos = {heap_root.id: (0, 0)}
    heap_graph = add_edges(heap_graph, heap_root, pos)

    colors = [node[1]['color'] for node in heap_graph.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in heap_graph.nodes(data=True)}	# Використовуйте значення вузла для міток

    plt.figure(figsize=(8, 5))
    nx.draw(heap_graph, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()


heap = Heap()

values = [10, 4, 1, 5, 0, 3, 12, 2]

for value in values:
    heap.add_node(Node(value, 'skyblue'))

draw_heap(heap)

