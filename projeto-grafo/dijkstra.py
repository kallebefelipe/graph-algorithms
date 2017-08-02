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


def gerar_menor_caminho(grafo_entrada, labels, no_origem, no_destino):
    graph = Graph()
    lista_nos = []
    for x, y in grafo_entrada:
        if x not in lista_nos:
            lista_nos.append(int(x))
            graph.add_node(int(x))
        if y not in lista_nos:
            lista_nos.append(int(y))
            graph.add_node(int(y))
        graph.add_edge(x, y, labels[(x, y)])
        graph.add_edge(y, x, labels[(x, y)])

    import ipdb; ipdb.set_trace()
    visited, path = dijsktra(graph, int(no_origem))
