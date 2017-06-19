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
        for each in linha:
            if each.isdigit() is False:
                nomes.append(each)
            else:
                sucessores.append(int(each))
        grafo.append(sucessores)
    return grafo, nomes, int(data[0])


def sucessores(no, grafo, nomes):
    if no in nomes:
        print('Sucessores de '+no+': ', end='')
        for each in grafo[nomes.index(no)][1:]:
            print(nomes[each]+', ', end='')
        print()
    else:
        print('No nao encontrado')


def nome_no(num, nomes):
    if num < len(nomes):
        return nomes[num]
    else:
        print('Tamanho maior do que grafo')


def busca_ciclo(grafo):
    for no in grafo:
        pass


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
    print('Granfo contem ciclo: ', end='')
    for node in range(V):
        if visited[node] is False:
            if isCyclicUtil(node, visited, recStack, graph) is True:
                print('sim')
                return True
    print('nao')
    return False


def is_paralelo(grafo):
    print('Grafo paralelo: ', end='')
    for no in grafo:
        lista = []
        for v in no:
            if v not in lista:
                lista.append(v)
            else:
                print('Sim')
                return None
    print('Nao')


def buscar_no(v, visited, recStack, graph, proximo):
    visited[v] = True

    for neighbour in graph[v]:
        if visited[neighbour] is False:
            if buscar_no(neighbour, visited, recStack, graph, proximo) is True:
                return True
        if v == proximo:
            return True

    return False


def fortemente_conectado(V, graph):
    print('Grafo fracamente conectado: ', end='')
    for node in range(V):
        visited = [False] * V
        recStack = [False] * V
        for proximo in range(node+1, V):
            if visited[node] is False:
                if buscar_no(node, visited, recStack, graph, proximo) is False:
                    return False

    for node in range(V-1, 0, -1):
        visited = [False] * V
        recStack = [False] * V
        for proximo in range(node-1, -1, -1):
            if visited[node] is False:
                if buscar_no(node, visited, recStack, graph, proximo) is False:
                    print('sim')
                    return False
    print('nao')
    return True


def tranposto(grafo, V):
    grafo_transposto = [None] * V

    for no in grafo:
        for vizinho in no[1:]:
            if grafo_transposto[vizinho] is None:
                grafo_transposto[vizinho] = [vizinho]
            grafo_transposto[vizinho].append(no[0])
    return grafo_transposto


group = 1


def percorrer(v, visited, graph, groups):
    global group
    visited[v] = True
    for neighbour in graph[v]:
        if groups[v] != 0:
            groups[neighbour] = groups[v]
        elif groups[neighbour]:
            groups[v] = groups[neighbour]
        else:
            group += 1
            groups[v] = group

        if visited[neighbour] is False:
            if percorrer(neighbour, visited, graph, groups) is True:
                return True

    return False


def componentes(V, graph):
    visited = [False] * V
    groups = [0] * V
    groups[0] = 1
    for node in range(V):
        if visited[node] is False:
            percorrer(node, visited, graph, groups)


data = leitura('data/entrada1.txt')
grafo, nomes, V = gerar_grafo(data)
# fortemente = fortemente_conectado(V, grafo)
# tranposto = tranposto(grafo, V)
print(componentes(V, grafo))
