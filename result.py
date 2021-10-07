import math


def calculate_result(vertices):
    vertices.sort()
    n = len(vertices)
    distances = [[0 for _ in range(n)] for _ in range(n)]  # n * n matrix

    for origin in vertices:
        for destination in vertices:
            distances[origin.id - 1][destination.id - 1] = origin.min_path_distance_to(destination)

    print()
    print_matrix(vertices, distances)
    print()
    print_distances(vertices, distances)


def print_matrix(vertices, distances):
    print("Min cost for going from X to Y:")
    print()
    print("     ", end="")
    for vertex in vertices:
        print(f" {vertex}  ", end="")
    print()

    for i in range(len(vertices)):
        print(f" {vertices[i]}  ", end="")
        for distance in distances[i]:
            print(f"{distance} ".rjust(4, " "), end="")
        print()


def print_distances(vertices, distances):
    min_distance = math.inf
    min_vertex = 0

    for i in range(len(vertices)):
        distance = sum(distances[i])
        print(f"Sum of distances from '{vertices[i]}' is {distance}")

        if distance < min_distance:
            min_distance = distance
            min_vertex = vertices[i]

    print()
    print(f"The point with minimum distance to everywhere else is '{min_vertex}' with total cost {min_distance}")
