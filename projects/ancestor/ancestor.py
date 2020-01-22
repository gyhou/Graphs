class Stack():
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None

    def size(self):
        return len(self.stack)


class Graph:
    """
    Represent a graph as a dictionary of vertices mapping labels to edges.
    """

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("That vertex does not exist.")


def earliest_ancestor(ancestors, starting_node):
    graph = Graph()
    for parent, child in ancestors:
        graph.add_vertex(parent)
        graph.add_vertex(child)
        # graph.add_edge(child, parent)
    for parent, child in ancestors:
        graph.add_edge(child, parent)

    stack = Stack()
    stack.push([starting_node])
    # Create an empty Set to store visited vertices
    visited = set()
    longest_path = [-1]
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
            visited.add(vertex)
            # Then add A PATH to its neighbors to the back of the queue
            for next_vert in graph.vertices[vertex]:
                # COPY THE PATH
                new_path = path.copy()
                # APPEND THE NEIGHBOR TO THE BACK
                new_path.append(next_vert)
                stack.push(new_path)

    return longest_path[-1]
