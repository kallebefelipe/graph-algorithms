from dijkstra import gerar_menor_caminho
'''
Funcao de leitura de arquivo txt
'''
def leitura(filename):
    with open(filename) as f:
        data = f.readlines()
        data = [x.replace('\n', '') for x in data]
        return data


'''
Funcao de geracao de grafo, a partir de dados de entrada do arquivo,
a montagem da lista de adjacencia é feita incluido valor do vertice atual,
ex: vertice 0 com vizinho 1, a lista de adjacencia sera [0, 1]. Todas
as outras funcoes sao implementadas levando isso em consideracao.
'''
def gerar_grafo(data):
    nomes = []
    grafo = [] * int(data[0])
    pesos = [] * int(data[0])

    for pos in range(1, int(data[0])+1):
        linha = data[pos]
        linha = linha.split(' ')

        sucessores = [pos-1]
        linha_peso = []
        nomes.append(linha[0])
        for count, each in enumerate(linha[1:]):
            if (count % 2) == 0:
                sucessores.append(int(each))
            else:
                linha_peso.append(int(each))
        grafo.append(sucessores)
        pesos.append(linha_peso)
    return grafo, pesos, nomes, int(data[0])

'''
Funcao que retorna sucessores de um vertice v, dado um grafo.
A primeria posicao da lista de adjacencia nao é incluido pois trata-se do
vertice v.
'''
def sucessores(v, grafo, pesos):
    lista_vizinhos = []
    if len(grafo[v]) > 1:
        for count, each in enumerate(grafo[v][1:]):
            lista_vizinhos.append({'sucessor': each, 'peso': pesos[v][count]})
    return v, lista_vizinhos


'''
Funcao que retorna valor true se existe aresta entre o vertice v e
o vertice y. Tambem é retornado os proprio parametro x e y, para
facilitar no print.
'''
def existe_arco(grafo, v, y):
    for vizinho in grafo[v]:
        if vizinho == y:
            return True, v, y
    return False, v, y


'''
Dado um vertice v esse funcao retorna o nome desse vertice em strint
'''
def nome_no(v, nomes):
    if v < len(nomes):
        return str(nomes[v]), v
    return '', ''


def peso_sucessores(x, y, grafo, pesos):
    return v, {'peso': pesos[x][grafo[x].index(y)-1]}


def somar_pesos(pesos, caminhos):
    soma = 0
    for y, x in caminhos:
        soma += pesos[x][grafo[x].index(y)-1]
    return soma


def mostrar_pontes(caminhos, nomes):
    for y, x in caminhos:
        print('\t('+nome_no(x, nomes)[0]+', '+nome_no(y, nomes)[0]+')')


def mostrar_caminhos(caminhos, lista_pesos, nomes):
    print(lista_pesos)
    for i in range(0, len(caminhos)):
        for count, caminho in enumerate(caminhos[:i+1]):
            if i == 0 or count == (i-1):
                print(nome_no(caminho[1], nomes)[0]+'->', end='')
            print(nome_no(caminho[0], nomes)[0]+'->', end='')
        print('(custo:'+str(lista_pesos[i+1])+')')


data = leitura('data/entrada1.txt') # arquivo de entrada do grafo
grafo, pesos, nomes, V = gerar_grafo(data)
v, sucessores = sucessores(0, grafo, pesos) # retorna o sucessor do vertice v (inteiro)
print('Os sucessores de '+nomes[v]+': '+str(sucessores)+'\n')

existe, x, y = existe_arco(grafo, 0, 1) # testa se existe vertice entro dois no x e y (inteiro)
print('Existe arco entre '+nomes[x]+' e '+nomes[y]+': '+str(existe)+'\n')

nome, x = nome_no(0, nomes)
print('O nome do no '+str(x)+': '+str(nome)+'\n')

x, y = (1, 3)
v, peso = peso_sucessores(x, y, grafo, pesos)
print('O peso entre os vertices '+str(x)+' e '+str(y)+': '+str(peso)+'\n')

lista_pesos, caminhos =  gerar_menor_caminho(grafo, pesos)
print('Pontes a serem reconstruidas:')
mostrar_pontes(caminhos, nomes)
print('Custo total:'+str(somar_pesos(pesos, caminhos)))

lista_pesos, caminhos =  gerar_menor_caminho(grafo, pesos)
print('Menores caminhos saindo de Recife:')
mostrar_caminhos(caminhos, lista_pesos, nomes)
