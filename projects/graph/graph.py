"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy


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

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # Create an empty queue and enqueue the starting vertex ID
        queue = Queue()
        queue.enqueue(starting_vertex)
        # Create an empty Set to store visited vertices
        visited = set()
        # While the que is not empty..
        while queue.size() > 0:
            # Deqeue the first vertex
            vertex = queue.dequeue()
            # If that vertex hasn't been visited..
            if vertex not in visited:
                # Mark it as visited
                # print(v)
                visited.add(vertex)
                # Then add all of its neighbors to the back of the queue
                # for neighbor in self.get_neighbors(v):
                for neighbor in self.vertices[vertex]:
                    queue.enqueue(neighbor)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # Create an empty stack and push the starting vertex ID
        stack = Stack()
        stack.push(starting_vertex)
        # Create an empty Set to store visited vertices
        visited = set()
        # While the stack is not empty..
        while stack.size() > 0:
            # Pop the first vertex
            vertex = stack.pop()
            # If that vertex hasn't been visited..
            if vertex not in visited:
                # Mark it as visited
                # print(v)
                visited.add(vertex)
                # Then add all of its neighbors to the top of the stack
                for neighbor in self.vertices[vertex]:
                    stack.push(neighbor)

    def dft_recursive(self, starting_vertex, visited=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        if visited is None:
            visited = set()
        visited.add(starting_vertex)
        print(starting_vertex)
        for child_vert in self.vertices[starting_vertex]:
            if child_vert not in visited:
                self.dft_recursive(child_vert, visited)
        # if starting_vertex not in visited:
        #     print(starting_vertex)
        #     visited.append(starting_vertex)
        #     for neighbor in self.vertices[starting_vertex]:
        #         self.dft_recursive(neighbor, visited)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # Create an empty queue and enqueue A PATH TO starting vertext ID
        queue = Queue()
        queue.enqueue([starting_vertex])
        # Create an empty Set to store visited vertices
        visited = set()
        # While the que is not empty..
        while queue.size() > 0:
            # Deqeue the first PATH
            path = queue.dequeue()
            vertex = path[-1]
            # Grab last vertex from the PATH
            # If that vertex hasn't been visited..
            if vertex not in visited:
                if vertex == destination_vertex:
                    return path
                # Mark it as visited
                # print(vertex)
                visited.add(vertex)
                # Then add A PATH to its neighbors to the back of the queue
                for neighbor in self.vertices[vertex]:
                    # COPY THE PATH
                    new_path = path.copy()
                    # APPEND THE NEIGHBOR TO THE BACK
                    new_path.append(neighbor)
                    queue.enqueue(new_path)

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # Create an empty stack and pop A PATH TO starting vertext ID
        stack = Stack()
        stack.push([starting_vertex])
        # Create an empty Set to store visited vertices
        visited = set()
        # While the que is not empty..
        while stack.size() > 0:
            # pop the first PATH
            path = stack.pop()
            # Grab last vertex from the PATH
            vertex = path[-1]
            # If that vertex hasn't been visited..
            if vertex not in visited:
                if vertex == destination_vertex:
                    return path
                # Mark it as visited
                # print(vertex)
                visited.add(vertex)
                # Then add A PATH to its neighbors to the back of the queue
                for next_vert in self.vertices[vertex]:
                    # COPY THE PATH
                    new_path = path.copy()
                    # APPEND THE NEIGHBOR TO THE BACK
                    new_path.append(next_vert)
                    stack.push(new_path)

    def dfs_recursive(self, starting_vertex, destination_vertex, visited=None, path=None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        if visited is None:
            visited = set()
        if path is None:
            path = []
        visited.add(starting_vertex)
        path = path + [starting_vertex]
        # print(starting_vertex)
        if starting_vertex == destination_vertex:
            return path
        for child_vert in self.vertices[starting_vertex]:
            if child_vert not in visited:
                new_path = self.dfs_recursive(
                    child_vert, destination_vertex, visited, path)
                if new_path:
                    return new_path
        return None


if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    # print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    # graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    # graph.dft(1)
    # graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    # print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    # print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
