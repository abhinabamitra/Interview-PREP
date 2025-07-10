from enum import StrEnum
from collections import defaultdict


class GraphType(StrEnum):
    """Representation Type for graph."""

    ADJ_LIST = "adj_list"
    ADJ_MATRIX = "adj_matrix"


class GraphDirection(StrEnum):
    """Direction for the graph."""

    DIRECTED = "directed"
    UNDIRECTED = "undirected"


class Graph:
    """Unified graph class supports all representations."""

    def __init__(
        self,
        num_vertices: int,
        graph_type: GraphType,
        direction: GraphDirection,
    ) -> None:
        """Initialise the graph."""
        self.num_vertices = num_vertices
        self.graph_type = graph_type
        self.direction = direction

        if self.graph_type == GraphType.ADJ_LIST:
            self.graph = defaultdict(list)

        elif self.graph_type == GraphType.ADJ_MATRIX:
            self.graph = [[0] * self.num_vertices for _ in range(num_vertices)]
        else:
            msg = "Unsupported graph type."
            raise ValueError(msg)

    def add_edge(self, u: int, v: int) -> None:
        """Add an edge between two nodes."""
        if u >= self.num_vertices and v >= self.num_vertices:
            msg = "Vertex out of bounds."
            raise ValueError(msg)

        if self.graph_type == GraphType.ADJ_LIST:
            self.graph[u].append(v)
            if self.direction == GraphDirection.UNDIRECTED:
                self.graph[v].append(u)
        else:
            self.graph[u][v] = 1
            if self.direction == GraphDirection.UNDIRECTED:
                self.graph[v][u] = 1

    @property
    def raw_graph(self) -> dict[list] | list:
        return self.graph

    def __str__(self) -> dict[list] | list:
        if self.graph_type == GraphType.ADJ_LIST:
            return "\n".join(f"{k}:{v}" for k, v in self.graph.items())
        else:
            return "\n".join(str(row) for row in self.graph)


if __name__ == "__main__":
    NUM_VERTICES = 5
    EDGES = [(0, 1), (0, 4), (1, 2), (1, 3), (1, 4), (2, 3), (3, 4)]

    configs = [
        ("Adjacency List Undirected", GraphType.ADJ_LIST, GraphDirection.UNDIRECTED),
        ("Adjacency List Directed", GraphType.ADJ_LIST, GraphDirection.DIRECTED),
        (
            "Adjacency Matrix Undirected",
            GraphType.ADJ_MATRIX,
            GraphDirection.UNDIRECTED,
        ),
        ("Adjacency Matrix Directed", GraphType.ADJ_MATRIX, GraphDirection.DIRECTED),
    ]

    for name, g_type, direction in configs:
        print(f"== {name} ==")
        g = Graph(NUM_VERTICES, graph_type=g_type, direction=direction)
        for u, v in EDGES:
            g.add_edge(u, v)
        print(g, end="\n\n")
