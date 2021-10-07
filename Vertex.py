import math


class Vertex:
    def __init__(self, name, id):
        self.name = name
        self.id = id + 1

        self.edges = []
        self.predecessors = []

        self.bellman_ford_min_path = 0
        self.dijkstra_distance = 0
        self.dijkstra_edge_parent = 0

        self.min_paths = {}

    def __str__(self):
        return self.name

    def __eq__(self, other):
        return self.id == other.id

    def __lt__(self, other):
        return self.id < other.id

    def min_path_distance_to(self, other_vertex):
        if other_vertex == self:
            return 0

        path = self.min_paths[other_vertex.id]
        if not path:
            return math.inf

        return sum([edge.weight for edge in path])
