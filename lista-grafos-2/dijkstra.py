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
    list_path = []

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
                for each in list_path:
                    if edge == each[0]:
                        list_path.remove(each)
                list_path.append((edge, min_node))

    return visited, list_path


def gerar_caminho(path, no_origem, no_destino, labels):
    encontrado = False
    inicio = True
    caminho = []
    novo_labels = {}
    while encontrado is not True:
        for x, y in path:
            if x == no_destino and inicio:
                proximo = y
                inicio = False
                caminho.append((x, y))
                if (x, y) in labels:
                    novo_labels[(x, y)] = labels[(x, y)]
                elif (y, x) in labels:
                    novo_labels[(y, x)] = labels[(y, x)]
                if y == no_origem:
                    encontrado = True

                break
            elif y == no_destino and inicio:
                proximo = x
                inicio = False
                caminho.append((x, y))
                if (x, y) in labels:
                    novo_labels[(x, y)] = labels[(x, y)]
                elif (y, x) in labels:
                    novo_labels[(y, x)] = labels[(y, x)]
                if x == no_origem:
                    encontrado = True
                break
            elif inicio is False:
                if x == proximo:
                    proximo = y
                    caminho.append((x, y))
                    if (x, y) in labels:
                        novo_labels[(x, y)] = labels[(x, y)]
                    elif (y, x) in labels:
                        novo_labels[(y, x)] = labels[(y, x)]
                    if y == no_origem:
                        encontrado = True
                    break

                elif y == proximo:
                    proximo = x
                    caminho.append((x, y))
                    if (x, y) in labels:
                        novo_labels[(x, y)] = labels[(x, y)]
                    elif (y, x) in labels:
                        novo_labels[(y, x)] = labels[(y, x)]
                    if x == no_origem:
                        encontrado = True
                    break
    return caminho, novo_labels


def excluir_caminho(grafo_entrada, labels, caminho, novo_labels):
    for each in novo_labels:
        del labels[each]
    for each in caminho:
        try:
            grafo_entrada.remove(each)
        except:
            grafo_entrada.remove((each[1], each[0]))
    return grafo_entrada, labels


def gerar_menor_caminho(grafo_entrada, labels):
    graph = Graph()
    for count, each in enumerate(grafo_entrada):
        graph.add_node(count)
        for vizinho in each[1:]:
            graph.add_edge(count, vizinho, labels[count][grafo_entrada[count].index(vizinho)-1])
            graph.add_edge(vizinho, count, labels[count][grafo_entrada[count].index(vizinho)-1])
    visited, path = dijsktra(graph, int(0))
    return visited, path
    # caminho, novo_labels = gerar_caminho(path, int(no_origem), int(no_destino), labels)
    # grafo_entrada, labels = excluir_caminho(grafo_entrada, labels,
    #                                         caminho, novo_labels)
    # return grafo_entrada, novo_labels, grafo_entrada, labels
