class Graph:
    def __init__(self, edges) -> None:
        self.v = len(edges)
        self.graph = []
        for i in range(self.v):
            for j in range(self.v):
                if edges[i][j] != 0:
                    self.graph.append([i, j, edges[i][j]])
    
    def default_dijkstra(self):
        self.shortest_path = [0] + [float('inf')] * (self.v - 1)
        for i in range(len(self.graph)):
            v, w, edge = self.graph[i]
            if self.shortest_path[w] == float('inf'):
                self.shortest_path[w] = self.shortest_path[v] + edge
            else:
                self.shortest_path[w] = min(self.shortest_path[w], self.shortest_path[v] + edge)
        return self.shortest_path

# edges = [
#     [0, 9, 0, 5, 2, 0],
#     [9, 0, 1, 8, 0, 0],
#     [0, 1, 0, 16, 0, 3],
#     [5, 8, 16, 0, 4, 5],
#     [2, 0, 0, 4, 0, 7],
#     [0, 0, 3, 5, 7, 0]
#     ]

edges = [
    [0, 1, 1, 1, 0, 5, 8],
    [1, 0, 0, 0, 4, 0, 8],
    [1, 0, 0, 3, 2, 6, 0],
    [1, 0, 2, 0, 0, 3, 0],
    [0, 4, 2, 0, 0, 1, 0],
    [0, 0, 6, 3, 1, 0, 4],
    [8, 8, 0, 0, 0, 4, 0]
]

g = Graph(edges)
s_p = g.default_dijkstra()
print(s_p)