import networkx as nx

class Vertex:
    def __init__(self, name):
        self.name = name
        self.edges = []

    def __str__(self):
        return f"{self.name}[{', '.join(str(edge) for edge in self.edges)}]"


class Edge:
    def __init__(self, vertex1, vertex2, weight):
        self.vertex1 = vertex1
        self.vertex2 = vertex2
        self.weight = weight

    def __str__(self):
        return f"{self.vertex1.name}{self.vertex2.name}({self.weight})"


class Graph:
    def __init__(self):
        self._vertices = []
        self._edges = []

    def get_nx_graph(self):
        G = nx.Graph()
        for edge in self._edges:
            G.add_edge(edge.vertex1.name, edge.vertex2.name, weight=edge.weight)
        return G

    def get_vertices(self):
        vertices_dict =  {}
        for vertex in self._vertices:
            vertices_dict[vertex.name] = {}
            for edge in vertex.edges:
                other_end = edge.vertex1 if edge.vertex1.name != vertex.name else edge.vertex2
                vertices_dict[vertex.name][other_end.name] = edge.weight
        return vertices_dict

    def get_edges(self):
        return self._edges

    def find_vertex(self, vertex_name: str):
        for vertex in self._vertices:
            if vertex.name == vertex_name:
                return vertex
        return None

    def add_vertex(self, vertex):
        self._vertices.append(vertex)

    def add_vertices(self, vertices):
        self._vertices.extend(vertices)

    def add_edge(self, vertex1, vertex2, weight):
        if isinstance(vertex1, Vertex):
            vertex1 = vertex1.name
        if isinstance(vertex2, Vertex):
            vertex2 = vertex2.name

        _v1 = self.find_vertex(vertex1)
        _v2 = self.find_vertex(vertex2)
        if _v1 is None:
            _v1 = Vertex(vertex1)
            self.add_vertex(_v1)
        if _v2 is None:
            _v2 = Vertex(vertex2)
            self.add_vertex(_v2)
        edge = Edge(_v1, _v2, weight)
        _v1.edges.append(edge)
        _v2.edges.append(edge)
        self._edges.append(edge)
