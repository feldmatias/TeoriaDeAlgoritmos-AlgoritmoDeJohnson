from Edge import Edge
from Vertex import Vertex
from bellman_ford_algorithm import bellman_ford_algorithm
from dijkstra_algorithm import dijkstra_algorithm


def johnson_algorithm(vertices):
    # First create a new vertex with edges to all other vertices with weight 0
    new_vertex = Vertex("Johnson", id=-1)
    new_edges = [Edge(new_vertex, vertex, 0) for vertex in vertices]
    for edge in new_edges:
        edge.vertex_to.predecessors.append(edge)

    # Apply Bellman Ford starting from new_vertex
    bellman_ford_algorithm([new_vertex] + vertices)

    # Remove created vertex and its edges
    for vertex in vertices:
        vertex.predecessors = vertex.predecessors[:-1]

    # Apply Dijkstra for every vertex
    for vertex in vertices:
        dijkstra_algorithm(vertices, vertex)
