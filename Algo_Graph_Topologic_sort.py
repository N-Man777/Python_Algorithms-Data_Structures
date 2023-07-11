# ONLY FOR DIRECTED ACYCLIC GRAPH!!!

def dfs(graph, s, visited, n):
    for w in graph[s]:
        if w not in visited:
            visited[w] = 0
            n = dfs(graph, w, visited, n)
    visited[s] = n
    return n-1
    

def topologic_sort(graph, start):
    n = len(graph)
    visited = {start: 0}
    top_sorted = dfs(graph, start, visited, n)
    return visited

graph = {
    'S': ["A", "B"],
    "A": ["C"],
    "B": ["C", "D"],
    "C": ["D", "E"],
    "D": ["E"],
    "E": [],    
}

top_sort = topologic_sort(graph, "S")
print(top_sort)