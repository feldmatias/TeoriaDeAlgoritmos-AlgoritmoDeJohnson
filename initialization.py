from Edge import Edge
from Vertex import Vertex


def parse_file(filename):
    data = []
    with open(filename) as f:
        for line in f.readlines():
            origin, destination, weight = line.split(',')
            data.append((origin, destination, int(weight)))
    return data


def create_graph(filename):
    data = parse_file(filename)
    vertices = {}

    for line in data:
        from_name, to_name, weight = line

        vertex_from = vertices.get(from_name, Vertex(from_name, id=len(vertices)))
        vertices[from_name] = vertex_from

        vertex_to = vertices.get(to_name, Vertex(to_name, id=len(vertices)))
        vertices[to_name] = vertex_to

        edge = Edge(vertex_from, vertex_to, weight)

        vertex_from.edges.append(edge)
        vertex_to.predecessors.append(edge)

    return list(vertices.values())
