def leitura(filename):
    with open(filename) as f:
        data = f.readlines()
        data = [x.replace('\n', '') for x in data]
        return data


def gerar_grafo(data):
    nomes = []
    grafo = [] * int(data[0])

    for pos in range(1, int(data[0])+1):
        linha = data[pos]
        linha = linha.split(' ')

        sucessores = [pos-1]
        nomes.append(linha[0])
        for each in linha[1:]:
            sucessores.append(int(each))
        grafo.append(sucessores)
    return grafo, nomes, int(data[0])


def sucessores(v, grafo):
    lista_vizinhos = []
    for each in grafo[v][1:]:
        lista_vizinhos.append(each)
    return v, lista_vizinhos


def existe_arco(grafo, v, y):
    for vizinho in grafo[v]:
        if vizinho == y:
            return True, v, y
    return False, v, y


def nome_no(v, nomes):
    if v < len(nomes):
        return nomes[v], v
    return '', ''


def isCyclicUtil(v, visited, recStack, graph):
    visited[v] = True
    recStack[v] = True

    for neighbour in graph[v][1:]:
        if visited[neighbour] is False:
            if isCyclicUtil(neighbour, visited, recStack, graph) is True:
                return True
        elif recStack[neighbour] is True:
            return True

    recStack[v] = False
    return False


def isCyclic(V, graph):
    visited = [False] * V
    recStack = [False] * V
    for node in range(V):
        if visited[node] is False:
            if isCyclicUtil(node, visited, recStack, graph) is True:
                return True
    return False


def has_parallel_arcs(grafo):
    for no in grafo:
        lista = []
        for v in no:
            if v not in lista:
                lista.append(v)
            else:
                return True
    return False


def buscar_no(v, visited, recStack, graph, proximo):
    visited[v] = True

    for neighbour in graph[v]:
        if visited[neighbour] is False:
            if buscar_no(neighbour, visited, recStack, graph, proximo) is True:
                return True
        if v == proximo:
            return True

    return False


# def fortemente_conectado(V, graph):
#     print('Grafo fracamente conectado: ', end='')
#     for node in range(V):
#         visited = [False] * V
#         recStack = [False] * V
#         for proximo in range(node+1, V):
#             if visited[node] is False:
#                 if buscar_no(node, visited, recStack, graph, proximo) is False:
#                     return False

#     for node in range(V-1, 0, -1):
#         visited = [False] * V
#         recStack = [False] * V
#         for proximo in range(node-1, -1, -1):
#             if visited[node] is False:
#                 if buscar_no(node, visited, recStack, graph, proximo) is False:
#                     print('sim')
#                     return False
#     print('nao')
#     return True


def tranposto(grafo, V):
    grafo_transposto = [None] * len(grafo)

    for no in grafo:
        for vizinho in no:
            if grafo_transposto[vizinho] is None:
                grafo_transposto[vizinho] = []
            grafo_transposto[vizinho].append(no[0])
    return grafo_transposto


def componentes(V, grafo):
    rotulo = []
    for count, each in enumerate(grafo):
        rotulo.append(count)

    for vertice in grafo:
        for arco in vertice[1:]:
            alpha = rotulo[vertice[0]]
            beta = rotulo[arco]
            if alpha != beta:
                for count, x in enumerate(rotulo):
                    if x == beta:
                        if beta < alpha:
                            rotulo[x] = beta
                            rotulo[vertice[0]] = beta
                        else:
                            rotulo[x] = alpha
    componente = []
    for each in rotulo:
        if each not in componente:
            componente.append(each)
    return len(componente)


data = leitura('data/entrada1.txt')
grafo, nomes, V = gerar_grafo(data)

v, sucessores = sucessores(0, grafo)
print('Os sucessores de '+nomes[v]+': '+str(sucessores)+'\n')

existe, x, y = existe_arco(grafo, 0, 1)
print('Existe arco entre '+nomes[x]+' e '+nomes[y]+': '+str(existe)+'\n')

nome, x = nome_no(0, nomes)
print('O nome do no '+str(x)+': '+str(nome)+'\n')

iscyclic = isCyclic(V, grafo)
print('Existe ciclo no grafo: '+str(iscyclic)+'\n')

arco_paralelo = has_parallel_arcs(grafo)
print('Existe arco paralelo: '+str(arco_paralelo)+'\n')
# fracamente

transposto = tranposto(grafo, V)
print('Grafo transposto:')
for each in transposto:
    print(each)
print()

qt_componente = componentes(V, grafo)
print('Neste grafo existe '+str(qt_componente)+' componentes')
