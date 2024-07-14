class Graph:
    def __init__(self, number):
        self.number = number
        self.adj = [[]*number for i in range(number)]
            
    def create_vertex(self, x, y):
        self.adj[x-1].append(y-1)
        self.adj[y-1].append(x-1)

    def Breadth_First_Search(self, source):
        result = []
        Queue = []
        Visited = [False]*self.number
        Queue.append(source)
        Visited[source] = True

        while len(Queue) > 0:
            s = Queue.pop(0)
            result.append(s)

            for node in self.adj[s]:
                if Visited[node] == False:
                    Queue.append(node)
                    Visited[node] = True

        print(result)

g = Graph(6)
g.create_vertex(1, 2)
g.create_vertex(1, 3)
g.create_vertex(2, 4)
g.create_vertex(3, 5)
g.create_vertex(2, 6)
#print(g.adj)
g.Breadth_First_Search(0)