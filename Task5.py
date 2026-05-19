import uuid

import networkx as nx
import matplotlib.pyplot as plt

from enum import Enum
from collections import deque

COLOR_MIXIN = (30,30,20)
START_COLOR = '#191d95'

class MixMode(Enum):
    ADD = 0
    MULTIPLY = 1

class Node:
    def __init__(self, key, color="#2b2bfb"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color	# Додатковий аргумент для зберігання кольору вузла
        self.id = str(uuid.uuid4())	# Унікальний ідентифікатор для кожного вузла


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

def byte_clamp(value):
    return  max(min(round(value), 255), 0)

def mix_color(color: str, operation: MixMode = MixMode.MULTIPLY) -> str:
    red = int(color[1:3], 16)
    green = int(color[3:5], 16)
    blue = int(color[5:7], 16)

    match operation:
        case MixMode.ADD:
            red += COLOR_MIXIN[0]
            green += COLOR_MIXIN[1]
            blue += COLOR_MIXIN[2]
        case MixMode.MULTIPLY:
            red *= COLOR_MIXIN[0]
            green *= COLOR_MIXIN[1]
            blue *= COLOR_MIXIN[2]
    return f'#{byte_clamp(red):02x}{byte_clamp(green):02x}{byte_clamp(blue):02x}'


def dfs_iterative(start_vertex):
    visited = set()

    stack = [start_vertex]
    color = START_COLOR

    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            print(vertex.val, end=' ')
            color = mix_color(color, operation=MixMode.ADD)
            vertex.color = color
            visited.add(vertex)
            children = []
            if vertex.left:
                children.append(vertex.left)
            if vertex.right:
                children.append(vertex.right)
            stack.extend(reversed(children))

def bfs_iterative(start_vertex):
    visited = set()
    queue = deque([start_vertex])
    color = START_COLOR

    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            color = mix_color(color, operation=MixMode.ADD)
            vertex.color = color
            visited.add(vertex)
            children = []
            if vertex.left:
                children.append(vertex.left)
            if vertex.right:
                children.append(vertex.right)
            children = [c for c in children if c not in visited]
            queue.extend(children)


def draw_tree(tree_root, method):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}	# Використовуйте значення вузла для міток
    fig = plt.figure(figsize=(8, 5))
    fig.canvas.manager.set_window_title(f"{method.upper()} traversal")

    nx.draw(tree, pos=pos, labels=labels, node_size=2500, node_color=colors)
    plt.show()

def main():

    allowed_options = ["bfs", "dfs"]
    user_input = ''
    while True:
        user_input = input("Enter either bfs or dfs: ").strip().lower()

        if user_input in allowed_options:
            break


    # Створення дерева
    root = Node(0)
    root.left = Node(4)
    root.left.left = Node(5)
    root.left.right = Node(10)
    root.right = Node(1)
    root.right.left = Node(3)

    if user_input == "bfs":
        bfs_iterative(root)
    elif user_input == "dfs":
        dfs_iterative(root)
    # Відображення дерева
    draw_tree(root, user_input)


if __name__ == '__main__':
    main()