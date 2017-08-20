# Python program to detect cycle
# in a graph

from collections import defaultdict


class Graph():
    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.V = vertices

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def isCyclicUtil(self, v, visited, recStack):

        # Mark current node as visited and
        # adds to recursion stack
        visited[v] = True
        recStack[v] = True
        # Recur for all neighbours
        # if any neighbour is visited and in
        # recStack then graph is cyclic
        for neighbour in self.graph[v]:
            if visited[neighbour] is False:
                if self.isCyclicUtil(neighbour, visited, recStack) is True:
                    return True
            elif recStack[neighbour] is True:
                return True

        # The node needs to be poped from
        # recursion stack before function ends
        recStack[v] = False
        return False

    # Returns true if graph is cyclic else false
    def isCyclic(self):
        visited = [False] * self.V
        recStack = [False] * self.V
        for node in range(self.V):
            if visited[node] is False:
                if self.isCyclicUtil(node, visited, recStack) is True:
                    return True
        return False


g = Graph(2)
g.addEdge(0, 1)

if g.isCyclic() is 1:
    print("Graph has a cycle")
else:
    print("Graph has no cycle")

# Thanks to Divyanshu Mehta for contributing this code
