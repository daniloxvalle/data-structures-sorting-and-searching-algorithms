# pylint: disable=redefined-outer-name

import sys
from heapq import heapify, heappush


class Node:
    def __init__(self, name):
        self.name = name
        # Set distance to infinity for all nodes
        self.cost = sys.maxsize
        # Mark all nodes unvisited
        self.visited = False
        # Predecessor
        self.pred = []


class Nodes:
    def __init__(self, nodes=None):
        if nodes is None:
            nodes = []
        self.nodes = nodes

    def __getitem__(self, name) -> Node:
        for node in self.nodes:
            if node.name == name:
                return node
        return None

    def append(self, node):
        self.nodes.append(node)

    def __len__(self):
        return len(self.nodes)

    def __str__(self) -> str:
        return str([node.name for node in self.nodes])


def dijsktra(graph, src_node, dest_node):
    nodes = Nodes()
    nodes.append(Node("A"))
    nodes.append(Node("B"))
    nodes.append(Node("C"))
    nodes.append(Node("D"))
    nodes.append(Node("E"))
    nodes.append(Node("F"))
    print("nodes", nodes)
    nodes[src_node].cost = 0
    # List of visited nodes
    visited = []
    # Node being visited
    current = src_node

    for _ in range(len(nodes) - 1):
        if current not in visited:
            visited.append(current)
            min_heap = []
            for j in graph[current]:
                if j not in visited:
                    cost = nodes[current].cost + graph[current][j]
                    if cost < nodes[j].cost:
                        nodes[j].cost = cost
                        nodes[j].pred = nodes[current].pred + [current]
                    heappush(min_heap, (nodes[j].cost, j))
                    print("min_heap", min_heap)
        heapify(min_heap)
        current = min_heap[0][1]
    print("Shortest Distance: " + str(nodes[dest_node].cost))
    print("Shortest Path: " + str(nodes[dest_node].pred + list(dest_node)))


if __name__ == "__main__":
    graph = {
        "A": {"B": 2, "C": 4},
        "B": {"A": 2, "C": 3, "D": 8},
        "C": {"A": 4, "B": 3, "E": 5, "D": 2},
        "D": {"B": 8, "C": 2, "E": 11, "F": 22},
        "E": {"C": 5, "D": 11, "F": 1},
        "F": {"D": 22, "E": 1},
    }

    SOURCE = "A"
    DESTINATION = "F"
    dijsktra(graph, SOURCE, DESTINATION)

# Dijkstra's Algorithm Explanation: https://www.youtube.com/watch?v=OrJ004Wid4o&t=125s
