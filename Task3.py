import heapq

from Graph import Graph

def dijkstra_orig(graph, start):
    vertices = graph.get_vertices()

    distances = {vertex: float("infinity") for vertex in vertices}
    previous_vertices = {vertex: None for vertex in vertices}
    distances[start] = 0

    heap = [(0, start)]

    while heap:
        current_distance, current_vertex = heapq.heappop(heap)

        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in vertices[current_vertex].food_items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_vertices[neighbor] = current_vertex
                heapq.heappush(heap, (distance, neighbor))

    return distances

def dijkstra(graph: Graph, start):
    distances = {vertex: float('infinity') for vertex in graph.get_vertices()}
    distances[start] = 0
    unvisited = graph.get_vertices()
    heap = [(0, start)]

    while heap:
        current_distance, current_vertex = heapq.heappop(heap)

        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in unvisited[current_vertex].food_items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(heap, (distance, neighbor))

    return distances



def main():
    graph = Graph()
    graph.add_edge('A', 'B', 10)
    graph.add_edge('B', 'C', 20)
    graph.add_edge('C', 'D', 10)
    graph.add_edge('A', 'D', 50)

    print(graph.get_nx_graph())
    print(dijkstra(graph, 'A'))




if __name__ == '__main__':
    main()
