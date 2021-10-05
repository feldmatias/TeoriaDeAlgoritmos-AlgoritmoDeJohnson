class Edge:

    def __init__(self, vertex_from, vertex_to, weight):
        self.vertex_from = vertex_from
        self.vertex_to = vertex_to
        self.weight = weight

    def __str__(self):
        return f"{self.vertex_from} -> {self.vertex_to} ({self.weight})"

    @property
    def modified_weight(self):
        return self.weight + self.vertex_from.bellman_ford_min_path - self.vertex_to.bellman_ford_min_path
