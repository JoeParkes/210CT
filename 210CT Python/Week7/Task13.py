graph = {
    'A': set(['B', 'C']), 
    'B': set(['A', 'D', 'E']),
    'C': set(['A', 'F']), 
    'D': set(['B', 'G']), 
    'E': set(['B', 'F', 'G']), 
    'F': set(['C', 'E']), 
    'G': set(['E', 'D'])}

def dfs(graph, start):
    visited, stack = set(), [start] 
    while stack:
        vertex = stack.pop(0) 
        if vertex not in visited:
            visited.add(vertex)
            stack.extend(graph[vertex] - visited) 
        return visited

print dfs(graph, 'A') # {'F', 'C', 'E', 'A', 'D', 'B', 'G'}

dfs(graph, 'A')