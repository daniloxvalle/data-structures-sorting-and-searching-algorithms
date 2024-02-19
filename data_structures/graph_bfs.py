# Breadth First Search or BFS for a Graph
# Busca em largura em um grafo (pt-BR)

# pylint: disable=redefined-outer-name


def bfs(visited, graph, node):
    visited.append(node)
    queue.append(node)

    while queue:
        s = queue.pop(0)
        print(s, end=" ")

        for neighbour in graph[s]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)


# Visited nodes (vertex)
visited = []
# Queue for BFS
queue = []

# Adjacency list
graph = {3: [2, 4], 4: [5, 6], 1: [2, 5], 6: [4], 5: [1, 2, 4], 2: [1, 5]}

#   3
#  / \
# 2   4 - 6
# | \ |
# 1 - 5

bfs(visited, graph, 3)

# Adjacency list
# graph = {5: [3, 7], 3: [2, 4], 7: [8], 2: [], 4: [8], 8: []}

#    5
#   / \
#  3   7
# / \   \
# 2  4 - 8

# bfs(visited, graph, 5)
