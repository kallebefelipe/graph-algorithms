from tkinter import *
import networkx as nx
import matplotlib.pyplot as plt
from dijkstra import gerar_menor_caminho
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


def leitura(filename):
    with open(filename) as f:
        data = f.readlines()
        data = [x.replace('\n', '').lower() for x in data]
        return data


def montar_grafo(data):
    nomes = []
    graph = []
    edge_labels = {}

    for pos in range(1, int(data[0])+1):
        linha = data[pos]
        linha = linha.split(' ')

        nomes.append(linha[0])

    for pos in range(1, int(data[0])+1):
        linha = data[pos]
        linha = linha.split(' ')

        for count, each in enumerate(linha[1:]):
            if (count % 2) == 0:
                graph.append((linha[0], nomes[int(each)]))
            else:
                edge_labels[graph[-1]] = int(each)
    return graph, edge_labels, nomes


class Application:
    def __init__(self, master=None):
        self.master = master
        self.figure = None
        self.fontePadrao = ("Arial", "10")
        self.primeiroContainer = Frame(master)
        self.primeiroContainer["pady"] = 10
        self.primeiroContainer.pack()

        self.segundoContainer = Frame(master)
        self.segundoContainer["padx"] = 20
        self.segundoContainer.pack()

        self.terceiroContainer = Frame(master)
        self.terceiroContainer["padx"] = 20
        self.terceiroContainer.pack()

        self.quartoContainer = Frame(master)
        self.quartoContainer["pady"] = 20
        self.quartoContainer.pack()
        self.titulo = Label(self.primeiroContainer, text="GPS")
        self.titulo["font"] = ("Arial", "10", "bold")
        self.titulo.pack()
        self.origemLabel = Label(self.segundoContainer, text="Origem", font=self.fontePadrao)
        self.origemLabel.pack(side=LEFT)

        self.origem = Entry(self.segundoContainer)
        self.origem["width"] = 30
        self.origem["font"] = self.fontePadrao
        self.origem.pack(side=LEFT)

        self.destinoLabel = Label(self.terceiroContainer, text="Destino", font=self.fontePadrao)
        self.destinoLabel.pack(side=LEFT)

        self.destino = Entry(self.terceiroContainer)
        self.destino["width"] = 30
        self.destino["font"] = self.fontePadrao
        self.destino.pack(side=LEFT)

        self.gera_caminho = Button(self.quartoContainer)
        self.gera_caminho["text"] = "Gerar caminho"
        self.gera_caminho["font"] = ("Calibri", "8")
        self.gera_caminho["width"] = 12
        self.gera_caminho["command"] = self.menor_caminho
        self.gera_caminho.pack()

        self.mensagem = Label(self.quartoContainer, text="", font=self.fontePadrao)
        self.mensagem.pack()

        data = leitura('data/entrada2.txt')
        self.graph, self.edge_labels, self.nomes = montar_grafo(data)
        self.restante_labels = None
        self.graph_pos = None
        self.save_graph, self.save_edge_labels = self.graph, self.edge_labels
        print(self.save_graph)
        print(self.save_edge_labels)

        self.gerar_grafo(self.graph, True)

    def menor_caminho(self):
        no_origem = self.origem.get()
        no_destino = self.destino.get()

        if no_origem not in self.nomes or no_destino not in self.nomes:
            self.mensagem["text"] = "Cidades invalidas !"
        else:
            self.graph, self.edge_labels = self.save_graph, self.save_edge_labels
            self.graph, self.edge_labels, \
                self.restante_graph, self.restante_labels = \
                gerar_menor_caminho(self.graph,
                                    self.edge_labels,
                                    no_origem,
                                    no_destino)
            self.gerar_grafo(self.graph, False)
            self.mensagem["text"] = "Caminho gerado !"

    def gerar_grafo(self, graph, first):
        # plt.close()
        G = nx.DiGraph()
        G.add_edges_from(graph, pos=0)
        if self.graph_pos is None:
            self.graph_pos = nx.spring_layout(G)

        nx.draw_networkx_nodes(G, self.graph_pos, node_size=1000, node_color='blue',
                               alpha=0.3)
        nx.draw_networkx_edges(G, self.graph_pos, edgelist=self.edge_labels, width=2, alpha=0.3,
                               edge_color='Red')
        if self.restante_labels is not None:
            nx.draw_networkx_edges(G, self.graph_pos, edgelist=self.restante_labels, width=2, alpha=0.3,
                                   edge_color='Green')
        nx.draw_networkx_labels(G, self.graph_pos, font_size=12,
                                font_family='sans-serif')

        nx.draw_networkx_edge_labels(G, self.graph_pos,
                                     edge_labels=self.edge_labels)
        if self.restante_labels is not None:
            nx.draw_networkx_edge_labels(G, self.graph_pos,
                                         edge_labels=self.restante_labels)

        pos = nx.get_node_attributes(G, 'pos')
        # plt.show()
        if first:
            fig =plt.gcf()
            self.canvas = FigureCanvasTkAgg(fig,master=self.master)
            self.canvas.show()
            self.canvas.get_tk_widget().pack(side='top', fill='both', expand=1)
            self.primeiroContainer.pack()
        else:
            self.master.attributes("-fullscreen", True)


root = Tk()
Application(root)
root.mainloop()
