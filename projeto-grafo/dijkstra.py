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


def remove_min(Q, c):
    min_Q = None
    for node in Q:
        if node in c:
            if min_Q is None:
                min_Q = node
            elif c[node] < c[min_Q]:
                min_Q = node
    if min_Q is not None:
        Q.remove(min_Q)
        return Q, min_Q
    else:
        return None, None


def decrease_key(Q, y, min_Q, ante):
    for each in ante:
        if y == each[0]:
            ante.remove(each)
    ante.append((y, min_Q))
    return ante


def initialize(G, s):
    c = {s: 0}
    for each in G.nodes:
        if each != s:
            c[each] = float('inf')
    return c


def dijsktra(G, s):
    c = initialize(G, s)

    ante = []

    Q = set(G.nodes)

    while Q:
        Q, x = remove_min(Q, c)

        if x is None:
            break

        for y in G.edges[x]:
            p = G.distances[(x, y)]
            if c[x] + p < c[y]:
                c[y] = c[x] + p
                print(ante)
                ante = decrease_key(Q, y, x, ante)
                print(ante)
                print()

    return c, ante


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
            lista_nos.append(x)
            graph.add_node(x)
        if y not in lista_nos:
            lista_nos.append(y)
            graph.add_node(y)
        graph.add_edge(x, y, labels[(x, y)])
        graph.add_edge(y, x, labels[(x, y)])

    visited, path = dijsktra(graph, no_origem)
    caminho, novo_labels = gerar_caminho(path, no_origem, no_destino, labels)
    grafo_entrada, labels = excluir_caminho(grafo_entrada, labels,
                                            caminho, novo_labels)
    return grafo_entrada, novo_labels, grafo_entrada, labels
