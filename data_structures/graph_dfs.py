# Depth First Search (DFS) implementation for graph traversal
# Busca em profundidade (DFS) para travessia de grafo (pt-BR)

# pylint: disable=redefined-outer-name


graph_letters = {
    "A": ["B", "C", "D"],
    "B": ["E"],
    "C": ["D", "E"],
    "D": ["E"],
    "E": [],
}

graph_numbers = {
    0: [1, 2, 3],
    1: [0, 3],
    2: [0, 3],
    3: [0, 1, 2, 4],
    4: [3],
}

visited = set()


def dfs(visited, graph, node):
    if node not in visited:
        print(node, end=" ")
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)


dfs(visited, graph_letters, "A")
print()
dfs(visited, graph_numbers, 0)
