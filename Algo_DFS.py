def dfs(graph, start):
    stack = [start]
    visited = set(start)
    while stack:
        current_vertex = stack.pop()
        for v in graph[current_vertex]:
            if v not in visited:
                stack.append(v)
                visited.add(v)
    return visited

def rec_dfs_2(graph, s, visited):
    for w in graph[s]:
        if w not in visited:
            visited.add(w)
            rec_dfs_2(graph, w, visited)




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

visited_s = dfs(graph, "S")
print("Visited vertices from 'S': {}".format(visited_s))
visited_f = dfs(graph, "F")
print("Visited vertices from 'F': {}".format(visited_f))

visited = {"F"}
rec_dfs_2(graph, "F", visited)
print("Visited vertices from 'F': {}".format(visited))