def default_dijkstra(graph, start):
    n = len(graph)
    shortest_path = [float("inf")] * n
    shortest_path[start] = 0
    visited = set()
    for _ in range(n):
        idx = None
        mn = float("inf")
        for i in range(n):
            if mn >= shortest_path[i] and i not in visited:
                mn = shortest_path[i]
                idx = i
        visited.add(idx)
        
        for w, edge in graph[idx]:
            if shortest_path[w] == float('inf'):
                shortest_path[w] = shortest_path[idx] + edge
            else:
                shortest_path[w] = min(shortest_path[w], shortest_path[idx] + edge)
    return shortest_path


graph = (
    ((1, 9), (3, 5), (4, 2)), 
         ((0, 9), (2, 1), (3, 8)), 
         ((1, 1), (3, 16), (5, 3)),
         ((0, 5), (1, 8), (2, 16), (4, 4), (5,5)),
         ((0, 2), (3, 4), (5, 7)),
         ((2, 3), (3, 5), (4, 7)))
