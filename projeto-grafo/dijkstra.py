import collections


class Graph:
    def __init__(self):
        self.nodes = set()
        self.edges = collections.defaultdict(list)
        self.distances = {}

    def add_node(self, value):
        self.nodes.add(value)

    def add_edge(self, from_node, to_node, distance):
        self.edges[from_node].append(to_node)
        self.edges[to_node].append(from_node)
        self.distances[(from_node, to_node)] = distance


def dijsktra(graph, initial):
    visited = {initial: 0}
    path = {}

    nodes = set(graph.nodes)

    while nodes:
        min_node = None
        for node in nodes:
            if node in visited:
                if min_node is None:
                    min_node = node
                elif visited[node] < visited[min_node]:
                    min_node = node

        if min_node is None:
            break

        nodes.remove(min_node)
        current_weight = visited[min_node]

        for edge in graph.edges[min_node]:
            weight = current_weight + graph.distances[(min_node, edge)]
            if edge not in visited or weight < visited[edge]:
                visited[edge] = weight
                path[edge] = min_node

    return visited, path


graph = Graph()
graph.add_node(1)
graph.add_node(2)
graph.add_node(3)
graph.add_node(4)
graph.add_node(5)
graph.add_node(6)
graph.add_edge(1, 6, 8)
graph.add_edge(6, 1, 8)
graph.add_edge(1, 3, 13)
graph.add_edge(3, 1, 13)
graph.add_edge(1, 5, 16)
graph.add_edge(5, 1, 16)
graph.add_edge(2, 6, 10)
graph.add_edge(6, 2, 10)
graph.add_edge(2, 4, 6)
graph.add_edge(4, 2, 6)
graph.add_edge(3, 4, 14)
graph.add_edge(4, 3, 14)
graph.add_edge(3, 6, 11)
graph.add_edge(6, 3, 11)
graph.add_edge(4, 6, 17)
graph.add_edge(6, 4, 17)
graph.add_edge(5, 4, 5)
graph.add_edge(4, 5, 5)
graph.add_edge(5, 6, 7)
graph.add_edge(6, 5, 7)
import ipdb; ipdb.set_trace()
visited, path = dijsktra(graph, 1)
