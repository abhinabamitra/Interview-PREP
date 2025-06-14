"""
A Python script to represent graph in all ways:
1. Adjacency List for Undirected Graph
2. Adjacency List for Directed Graph
3. Adjacency Matrix for Undirected Graph
4. Adjacency Matrix for Directed Graph
"""

from collections import defaultdict


class AdjacencyListUndirectedGraph:
    """Adjacency List for Undirected Graph."""

    def __init__(self, num_vertices: int) -> None:
        """Initializes the graph with fixed number of vertices."""
        self.num_vertices = num_vertices
        self.adj_list = defaultdict(list)

    def add_edge(self, u: int, v: int) -> None:
        """Add an undirected graph between vertex u and v."""
        if u > self.num_vertices or v > self.num_vertices:
            raise ValueError("Error out of bounds.")
        self.adj_list[u].append(v)
        self.adj_list[v].append(u)

    @property
    def notation(self) -> dict:
        return self.adj_list


class AdjacencyListDirectedGraph:
    """Adjacency List for Undirected Graph."""

    def __init__(self, num_vertices: int) -> None:
        """Initializes graph with fixed nodes."""
        self.num_vertices = num_vertices
        self.adj_list = defaultdict(list)

    def add_edge(self, u: int, v: int) -> None:
        """Add an directed graph between vertex u and v."""
        if u > self.num_vertices or v > self.num_vertices:
            raise ValueError("Error out of bounds.")
        self.adj_list[u].append(v)

    @property
    def notation(self) -> dict:
        return self.adj_list


class AdjacencyMatrixUndirectedGraph:
    """Adjacency Matrix for Undirected Graph."""

    def __init__(self, num_vertices: int) -> None:
        """Initializes the graph with fixed number of vertices."""
        self.num_vertices = num_vertices
        self.adj_matrix = [[0] * num_vertices for _ in range(num_vertices)]

    def add_edge(self, u: int, v: int) -> None:
        """Add an undirected edge in matrix."""
        if u > self.num_vertices or v > self.num_vertices:
            raise ValueError("Error out of bounds.")
        self.adj_matrix[u][v] = 1
        self.adj_matrix[v][u] = 1

    @property
    def notation(self) -> list:
        return self.adj_matrix


class AdjacencyMatrixDirectedGraph:
    """Adjacency Matrix for Undirected Graph."""

    def __init__(self, num_vertices: int) -> None:
        """Initializes the graph with fixed number of vertices."""
        self.num_vertices = num_vertices
        self.adj_matrix = [[0] * num_vertices for _ in range(num_vertices)]

    def add_edge(self, u: int, v: int) -> None:
        """Add an undirected edge in matrix."""
        if u > self.num_vertices or v > self.num_vertices:
            raise ValueError("Error out of bounds.")
        self.adj_matrix[u][v] = 1

    @property
    def notation(self) -> list:
        return self.adj_matrix


if __name__ == "__main__":
    NUM_VERTICES = 5
    EDGES = [(0, 1), (0, 4), (1, 2), (1, 3), (1, 4), (2, 3), (3, 4)]

    all_combinations = [
        AdjacencyListUndirectedGraph,
        AdjacencyMatrixUndirectedGraph,
        AdjacencyListDirectedGraph,
        AdjacencyMatrixDirectedGraph,
    ]

    for cls in all_combinations:
        graph = cls(NUM_VERTICES)
        for u, v in EDGES:
            graph.add_edge(u, v)

        print(cls.__name__)
        print(graph.notation)
        print("\n")
