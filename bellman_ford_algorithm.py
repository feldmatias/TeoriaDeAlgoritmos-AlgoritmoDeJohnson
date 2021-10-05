import math


def bellman_ford_algorithm(vertices):
    n = len(vertices)  # Maximum path length is n - 1
    optimal_paths = [[math.inf for _ in range(n)] for _ in range(n)]  # n * n matrix

    # Initialize matrix
    for i in range(n):
        optimal_paths[i][0] = 0

    # Apply algorithm
    for path_length in range(1, n):
        for vertex in vertices:

            # Optimal path with current length - 1
            vertex_optimal = optimal_paths[path_length - 1][vertex.id]

            # Optimal path for predecessors with current length - 1 + edge weight
            for predecessor_edge in vertex.predecessors:
                predecessor_optimal = optimal_paths[path_length - 1][predecessor_edge.vertex_from.id] + predecessor_edge.weight
                if predecessor_optimal < vertex_optimal:
                    vertex_optimal = predecessor_optimal

            # Store the minimum path in current length
            optimal_paths[path_length][vertex.id] = vertex_optimal

    # Store results
    for vertex in vertices:
        vertex.bellman_ford_min_path = optimal_paths[n - 1][vertex.id]
