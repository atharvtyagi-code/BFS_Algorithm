class Graph:
    def __init__(self, number):
        self.number = number
        self.adj = [[]*number for i in range(number)]
            
    def create_vertex(self, x, y):
        self.adj[x-1].append(y-1)
        self.adj[y-1].append(x-1)

    def Depth_First_Search(self, source):
        result = []
        Visited = [False]*self.number
        self.dfs_utility(source, Visited, result)
        print(result)

    def dfs_utility(self, source, Visited, result):
        result.append(source)
        Visited[source] = True

        for node in self.adj[source]:
            if not Visited[node]:
                self.dfs_utility(node, Visited, result)

g = Graph(6)
g.create_vertex(1, 4)
g.create_vertex(1, 2)
g.create_vertex(2, 3)
g.create_vertex(3, 5)
g.create_vertex(2, 6)
g.Depth_First_Search(0)