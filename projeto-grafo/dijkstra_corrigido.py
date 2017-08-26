
def Dijkstra(G, start, end=None):

    D = {}
    P = {}
    Q = {}
    for each in G:
        Q[each] = float("+infinity")
    Q[start] = 0
    for v in Q:
        D[v] = Q[v]

        for w in G[v]:
            vwLength = D[v] + G[v][w]
            if w not in Q or vwLength < Q[w]:
                Q[w] = vwLength
                P[w] = v

    return (D, P)


def shortestPath(G, start, end):

    D, P = Dijkstra(G, start, end)
    Path = []
    while 1:
        Path.append(end)
        if end == start:
            break
        end = P[end]
    Path.reverse()
    return Path


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
    G = {}
    for x, y in grafo_entrada:
        if x not in G:
            G[x] = {y: labels[(x, y)]}

    visited, path = Dijkstra(G, no_origem)
    import ipdb; ipdb.set_trace()
    caminho, novo_labels = gerar_caminho(path, no_origem, no_destino, labels)
    grafo_entrada, labels = excluir_caminho(grafo_entrada, labels,
                                            caminho, novo_labels)
    return grafo_entrada, novo_labels, grafo_entrada, labels
