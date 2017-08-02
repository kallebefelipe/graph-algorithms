from tkinter import *
import networkx as nx
import matplotlib.pyplot as plt
from dijkstra import gerar_menor_caminho


class Application:
    def __init__(self, master=None):
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
        self.origemLabel = Label(self.segundoContainer,text="Origem", font=self.fontePadrao)
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
        self.graph = [
            (1, 6), (1, 3), (1, 5), (2, 6), (2, 4),
            (3, 4), (3, 6), (4, 6), (5, 4), (5, 6)
        ]
        self.edge_labels = {(1, 6): 8, (1, 3): 13, (1, 5): 16, (2, 6): 10, (2, 4): 6,
                            (3, 4): 14, (3, 6): 11, (4, 6): 17, (5, 4): 5, (5, 6): 7}
        self.restante_labels = None

        self.gerar_grafo(self.graph)

    def menor_caminho(self):
        no_origem = self.origem.get()
        no_destino = self.destino.get()
        # try:
        self.graph, self.edge_labels, \
            self.restante_graph, self.restante_labels = \
            gerar_menor_caminho(self.graph,
                                self.edge_labels,
                                no_origem,
                                no_destino)
        self.gerar_grafo(self.graph)
        self.mensagem["text"] = "Caminho gerado !"
        # except:
        #     self.mensagem["text"] = "Informe enderenços válidos !"

    def gerar_grafo(self, graph):
        plt.close()
        G = nx.DiGraph()

        G.add_edges_from(graph)

        graph_pos = nx.spring_layout(G)
        # graph_pos = nx.spectral_layout(G)

        nx.draw_networkx_nodes(G, graph_pos, node_size=1000, node_color='blue',
                               alpha=0.3)
        nx.draw_networkx_edges(G, graph_pos, edgelist=self.edge_labels, width=2, alpha=0.3,
                               edge_color='Red')
        if self.restante_labels is not None:
            nx.draw_networkx_edges(G, graph_pos, edgelist=self.restante_labels, width=2, alpha=0.3,
                                   edge_color='Grey')
        nx.draw_networkx_labels(G, graph_pos, font_size=12,
                                font_family='sans-serif')

        nx.draw_networkx_edge_labels(G, graph_pos,
                                     edge_labels=self.edge_labels)
        if self.restante_labels is not None:
            nx.draw_networkx_edge_labels(G, graph_pos,
                                         edge_labels=self.restante_labels)
        plt.show()


root = Tk()
Application(root)
root.mainloop()
