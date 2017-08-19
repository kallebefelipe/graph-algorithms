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

    visited, path = dijsktra(graph, int(no_origem))
    caminho, novo_labels = gerar_caminho(path, int(no_origem), int(no_destino), labels)
    grafo_entrada, labels = excluir_caminho(grafo_entrada, labels,
                                            caminho, novo_labels)
    return grafo_entrada, novo_labels, grafo_entrada, labels
