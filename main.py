import sys

from initialization import create_graph
from johnson_algorithm import johnson_algorithm
from result import calculate_result

if __name__ == '__main__':
    if len(sys.argv) <= 1:
        print("Please enter file name.")
        print("Usage: `python main.py <filename>`")
    else:
        vertices = create_graph(sys.argv[1])
        johnson_algorithm(vertices)
        calculate_result(vertices)
