from tkinter import *
import networkx as nx
import matplotlib.pyplot as plt


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
        self.nomeLabel = Label(self.segundoContainer,text="Origem", font=self.fontePadrao)
        self.nomeLabel.pack(side=LEFT)

        self.nome = Entry(self.segundoContainer)
        self.nome["width"] = 30
        self.nome["font"] = self.fontePadrao
        self.nome.pack(side=LEFT)

        self.senhaLabel = Label(self.terceiroContainer, text="Destino", font=self.fontePadrao)
        self.senhaLabel.pack(side=LEFT)

        self.senha = Entry(self.terceiroContainer)
        self.senha["width"] = 30
        self.senha["font"] = self.fontePadrao
        self.senha.pack(side=LEFT)

        self.autenticar = Button(self.quartoContainer)
        self.autenticar["text"] = "Gerar caminho"
        self.autenticar["font"] = ("Calibri", "8")
        self.autenticar["width"] = 12
        self.autenticar["command"] = self.verificaSenha
        self.autenticar.pack()

        self.mensagem = Label(self.quartoContainer, text="", font=self.fontePadrao)
        self.mensagem.pack()
        graph = [
            (20, 21), (21, 22), (22, 23), (23, 24), (24, 25), (25, 20),
            (25, 21), (23, 20), (24, 22), (21, 24), (20, 21)
        ]

        self.gerar_grafo(graph)

    #Método verificar senha
    def verificaSenha(self):
        usuario = self.nome.get()
        senha = self.senha.get()
        graph = [
            (2, 21), (21, 22), (22, 23), (23, 24), (24, 25), (25, 20)
        ]
        self.gerar_grafo(graph)
        if usuario == "usuariodevmedia" and senha == "dev":
            self.mensagem["text"] = "Autenticado"
        else:
            self.mensagem["text"] = "Erro na autenticação"

    def gerar_grafo(self, graph):
        plt.close()
        G = nx.DiGraph()

        # add edges
        G.add_edges_from(graph)

        # graph_pos = nx.spring_layout(G)
        graph_pos = nx.spectral_layout(G)

        # draw nodes, edges and labels
        nx.draw_networkx_nodes(G, graph_pos, node_size=1000, node_color='blue',
                               alpha=0.3)
        # we can now added edge thickness and edge color
        nx.draw_networkx_edges(G, graph_pos, width=2, alpha=0.3, edge_color='green')
        nx.draw_networkx_labels(G, graph_pos, font_size=12, font_family='sans-serif')

        labels = range(len(graph))
        # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

        edge_labels = dict(zip(graph, labels))
        # {(23, 20): 7, (22, 23): 2, (20, 21): 10, (24, 25): 4, (21, 22): 1, (25, 20): 5, (24, 22): 8, (25, 21): 6, (23, 24): 3, (21, 24): 9}

        nx.draw_networkx_edge_labels(G, graph_pos, edge_labels=edge_labels)
        # show graph

        plt.show()
        plt.get_tk_widget().pack(side=master.TOP, fill=master.BOTH, expand=True)


root = Tk()
Application(root)
root.mainloop()
