import math
from queue import PriorityQueue


def dijkstra_algorithm(vertices, starting_vertex):
    # Initialization
    heap = PriorityQueue()
    visited = set()
    for vertex in vertices:
        vertex.dijkstra_edge_parent = None
        vertex.dijkstra_distance = math.inf
        if vertex == starting_vertex:
            vertex.dijkstra_distance = 0
            heap.put((vertex.dijkstra_distance, vertex))

    # Apply algorithm
    while not heap.empty():
        _, min_vertex = heap.get()
        if min_vertex.id in visited:
            # Ignore it because it already has a minimum path
            continue
        visited.add(min_vertex.id)

        # Calculate distance path for neighbours if coming from min_vertex
        for edge in min_vertex.edges:
            neighbour = edge.vertex_to
            new_distance = min_vertex.dijkstra_distance + edge.modified_weight
            if new_distance < neighbour.dijkstra_distance:
                # Current path is better
                neighbour.dijkstra_distance = new_distance
                neighbour.dijkstra_edge_parent = edge
                heap.put((neighbour.dijkstra_distance, neighbour))

    # Build min paths
    for vertex in vertices:
        path = []
        current_vertex = vertex

        # Rebuild the path going backwards
        while current_vertex:
            if current_vertex.dijkstra_edge_parent:
                path.insert(0, current_vertex.dijkstra_edge_parent)
                current_vertex = current_vertex.dijkstra_edge_parent.vertex_from
            else:
                current_vertex = None
        starting_vertex.min_paths[vertex.id] = path
