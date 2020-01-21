from graph import Graph
from util import Stack, Queue


def earliest_ancestor(ancestors, starting_node):
    vertices = set()
    for ancestor in ancestors:
        for vertex in ancestor:
            vertices.add(vertex)

    graph = Graph()
    for vertex in vertices:
        graph.add_vertex(vertex)
    for parent, child in ancestors:
        graph.add_edge(child, parent)

    stack = Stack()
    stack.push([starting_node])
    # Create an empty Set to store visited vertices
    visited = set()
    longest_path = []
    # While the que is not empty..
    while stack.size() > 0:
        # pop the first PATH
        path = stack.pop()
        # Grab last vertex from the PATH
        vertex = path[-1]
        # If that vertex hasn't been visited..
        if vertex not in visited:
            if len(path) > len(longest_path):
                longest_path = path.copy()
            elif len(path) == len(longest_path):
                if path[-1] < longest_path[-1]:
                    longest_path = path.copy()
            # Mark it as visited
            # print(vertex)
            visited.add(vertex)
            # Then add A PATH to its neighbors to the back of the queue
            for next_vert in graph.vertices[vertex]:
                # COPY THE PATH
                new_path = path.copy()
                # APPEND THE NEIGHBOR TO THE BACK
                new_path.append(next_vert)
                stack.push(new_path)

    if len(longest_path) == 1:
        return -1
    else:
        return longest_path[-1]
