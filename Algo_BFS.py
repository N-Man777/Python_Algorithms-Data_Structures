def bfs(graph:dict, start:str) -> None:
    queue = [start]
    visited = {start: 0}
    counter = 1
    while queue:
        current_vertex = queue.pop()
        for v in graph[current_vertex]:
            if v not in visited:
                queue.insert(0, v)
                visited[v] = visited[current_vertex] + 1  
    return visited


graph = {
    'S': ["A", "B"],
    "A": ["S", "C"],
    "B": ["S", "C", "D"],
    "C": ["A", "B", "D", "E"],
    "D": ["C", "E"],
    "E": ["C", "D"],
    "F": ["G"],
    "G": ["F"],
    "H": ["I", "J"],
    "I": ["H", "J"],
    "J": ["H", "I"],    
}
# BFS algorithm + distances from the starting vertex to each (all edge weights are equal to 1)
visited_s = bfs(graph, "S")
print("Visited vertices from 'S': {}".format(visited_s))
visited_f = bfs(graph, "F")
print("Visited vertices from 'F': {}".format(visited_f))

# The BFS algorithm in the problem of connected components of an undirected graph
connected_components = dict()
counter = 1
visited = set()
for v in graph:
    if v not in visited:
        tmp = bfs(graph, v)
        [visited.add(k) for k in tmp.keys()]
        connected_components[counter] = tmp.keys()
        counter += 1

print("CONNECTED COMPONENTS in the UNDIRECTED GRAPH")
print(connected_components)