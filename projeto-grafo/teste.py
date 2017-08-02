#---------Imports
from numpy import arange, sin, pi
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import tkinter as Tk
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import networkx as nx
import matplotlib.pyplot as plt
#---------End of imports

graph = graph = [
(20, 21), (21, 22), (22, 23), (23, 24), (24, 25), (25, 20),
(25, 21), (23, 20), (24, 22), (21, 24), (20, 21)
]
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
# plt.get_tk_widget().pack(side=master.TOP, fill=master.BOTH, expand=True)

fig = plt.Figure()

x = np.arange(0, 2*np.pi, 0.01)        # x-array

def animate(i):
    line.set_ydata(np.sin(x+i/10.0))  # update the data
    return line,

root = Tk.Tk()

label = Tk.Label(root,text="SHM Simulation").grid(column=0, row=0)

canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().grid(column=0,row=1)
plt.show()

ax = fig.add_subplot(111)
line, = ax.plot(x, np.sin(x))
# ani = animation.FuncAnimation(fig, animate, np.arange(1, 200), interval=25, blit=False)

Tk.mainloop()
