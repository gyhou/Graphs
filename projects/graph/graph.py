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
        q = Queue()
        q.enqueue(starting_vertex)
        # Create an empty Set to store visited vertices
        visited = set()
        # While the que is not empty..
        while q.size() > 0:
            # Deqeue the first vertex
            v = q.dequeue()
            # If that vertex hasn't been visited..
            if v not in visited:
                # Mark it as visited
                # print(v)
                visited.add(v)
                # Then add all of its neighbors to the back of the queue
                # for neighbor in self.get_neighbors(v):
                for neighbor in self.vertices[v]:
                    q.enqueue(neighbor)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # Create an empty stack and push the starting vertex ID
        s = Stack()
        s.push(starting_vertex)
        # Create an empty Set to store visited vertices
        visited = set()
        # While the stack is not empty..
        while s.size() > 0:
            # Pop the first vertex
            v = s.pop()
            # If that vertex hasn't been visited..
            if v not in visited:
                # Mark it as visited
                # print(v)
                visited.add(v)
                # Then add all of its neighbors to the top of the stack
                for neighbor in self.vertices[v]:
                    s.push(neighbor)

    def dft_recursive(self, starting_vertex, visited=[]):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        if starting_vertex not in visited:
            print(starting_vertex)
            visited.append(starting_vertex)
            for neighbor in self.vertices[starting_vertex]:
                self.dft_recursive(neighbor, visited)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # Create an empty queue and enqueue A PATH TO starting vertext ID
        q = Queue()
        path = [starting_vertex]
        q.enqueue(path)
        # Create an empty Set to store visited vertices
        visited = set()
        # While the que is not empty..
        while q.size() > 0:
            # Deqeue the first PATH
            v = q.dequeue()
            # Grab last vertex from the PATH
            # If that vertex hasn't been visited..
            if v[-1] not in visited:
                if v[-1] == destination_vertex:
                    return v
                # Mark it as visited
                # print(v)
                visited.add(v[-1])
                # Then add A PATH to its neighbors to the back of the queue
                for neighbor in self.vertices[v[-1]]:
                    # COPY THE PATH
                    v_copy = v.copy()
                    # APPEND THE NEIGHBOR TO THE BACK
                    v_copy.append(neighbor)
                    q.enqueue(v_copy)

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # Create an empty stack and pop A PATH TO starting vertext ID
        s = Stack()
        path = [starting_vertex]
        s.push(path)
        # Create an empty Set to store visited vertices
        visited = set()
        # While the que is not empty..
        while s.size() > 0:
            # pop the first PATH
            v = s.pop()
            # Grab last vertex from the PATH
            # If that vertex hasn't been visited..
            if v[-1] not in visited:
                if v[-1] == destination_vertex:
                    return v
                # Mark it as visited
                # print(v)
                visited.add(v[-1])
                # Then add A PATH to its neighbors to the back of the queue
                for neighbor in self.vertices[v[-1]]:
                    # COPY THE PATH
                    v_copy = v.copy()
                    # APPEND THE NEIGHBOR TO THE BACK
                    v_copy.append(neighbor)
                    s.push(v_copy)

    def dfs_recursive(self, starting_vertex, destination_vertex, visited=set()):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """

        if type(starting_vertex) is not list:
            starting_vertex = [starting_vertex]
        # print(starting_vertex[-1], destination_vertex)
        if starting_vertex[-1] == destination_vertex:
            # print(starting_vertex)
            return starting_vertex
        elif starting_vertex[-1] not in visited:
            if starting_vertex[-1] == destination_vertex:
                # print(starting_vertex)
                return starting_vertex
            else:
                # print(starting_vertex)
                visited.add(starting_vertex[-1])
                # print(visited)
                for neighbor in self.vertices[starting_vertex[-1]]:
                    # print(neighbor)
                    v_copy = starting_vertex.copy()
                    v_copy.append(neighbor)
                    if v_copy[-1] == destination_vertex:
                        print(v_copy)
                        return v_copy
                    else:
                        self.dfs_recursive(v_copy, destination_vertex, visited)


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
