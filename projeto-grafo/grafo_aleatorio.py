from random import randint


def gerar_grafo_aleatorio():
    tamanho = randint(4, 8)
    graph = []
    edge_labels = {}
    for i in range(1, tamanho):
        no1 = i
        no2 = randint(1, tamanho)
        while no2 == no1:
            no2 = randint(1, tamanho)
        graph.append((no1, no2))
        no1 = i
        no2 = randint(1, tamanho)
        while no2 == no1:
            no2 = randint(1, tamanho)
        graph.append((no1, no2))

    for each in graph:
        edge_labels[each] = randint(1, 20)
    return graph, edge_labels
