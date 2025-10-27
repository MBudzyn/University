from typing import List, Tuple
import random


def get_edges(graph: List[List[int]]) -> List[Tuple[int, int, int]]:
    edges = []
    for i in range(len(graph)):
        for j in range(i + 1, len(graph[i])):
            if graph[i][j] > 0:
                edges.append((i, j, graph[i][j]))
    return edges


def get_adjacency_list(edges: List[Tuple[int, int, int]]) -> dict[int, List[int]]:
    graph_dict = {}
    for u, v, _ in edges:
        if u not in graph_dict:
            graph_dict[u] = []
        if v not in graph_dict:
            graph_dict[v] = []
        graph_dict[u].append(v)
        graph_dict[v].append(u)
    return graph_dict


class Graph:
    def __init__(self, graph: List[List[int]]):
        self.graph = graph
        self.edges = get_edges(graph)
        self.number_of_vertices = len(graph)
        self.dfs_path = []

    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    def union(self, parent, rank, x, y):
        root_x = self.find(parent, x)
        root_y = self.find(parent, y)
        if rank[root_x] < rank[root_y]:
            parent[root_x] = root_y
        elif rank[root_x] > rank[root_y]:
            parent[root_y] = root_x
        else:
            parent[root_y] = root_x
            rank[root_x] += 1

    def get_mst(self) -> List[Tuple[int, int, int]]:
        edges = self.edges.copy()
        edges.sort(key=lambda x: x[2])
        parent = list(range(self.number_of_vertices))
        rank = [0] * self.number_of_vertices
        mst = []

        for u, v, weight in edges:
            root_u = self.find(parent, u)
            root_v = self.find(parent, v)
            if root_u != root_v:
                mst.append((u, v, weight))
                self.union(parent, rank, root_u, root_v)

        return mst

    def dfs(self, graph: dict[int, List[int]], start: int, visited=None):
        if visited is None:
            visited = set()
        visited.add(start)
        self.dfs_path.append(start)
        for neighbor in graph[start]:
            if neighbor not in visited:
                self.dfs(graph, neighbor, visited)

    def get_tsp_approximation_path(self) -> List[int]:
        visited = set()
        result = []
        for v in self.dfs_path:
            if v not in visited:
                result.append(v)
                visited.add(v)
        result.append(result[0])
        return result

    def run(self):
        mst = self.get_mst()
        graph_dict = get_adjacency_list(mst)
        self.dfs(graph_dict, 0)
        return self.get_tsp_approximation_path()


if __name__ == "__main__":
    size = 5
    graph = [[0 for _ in range(size)] for _ in range(size)]

    for i in range(size):
        for j in range(i + 1, size):
            weight = random.randint(1, 10)
            graph[i][j] = weight
            graph[j][i] = weight

    print("Full graph adjacency matrix:")
    for row in graph:
        print(row)

    g = Graph(graph)
    tsp_path = g.run()
    print("DFS Path:", g.dfs_path)
    print("Approximate TSP Path:", tsp_path)




