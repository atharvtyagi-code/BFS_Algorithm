class Graph:
    def __init__(self, number):
        self.number = number
        self.adj = [[]*number for i in range(number)]
            
    def create_vertex(self, x, y):
        self.adj[x-1].append(y-1)
        self.adj[y-1].append(x-1)

g = Graph(5)
g.create_vertex(1, 2)
g.create_vertex(1, 3)
g.create_vertex(2, 3)
g.create_vertex(2, 4)
g.create_vertex(1, 4)
print(g.adj)