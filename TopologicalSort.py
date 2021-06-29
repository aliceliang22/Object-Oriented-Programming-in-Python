#  File: TopologicalSory.py
#  Description: HW 17
#  Student Name: Alice Liang
#  Student UT EID: axl84
#  Course Name: CS 313E
#  Unique Number: 84825
#  Date Created: 08/8/20
#  Date Last Modified: 08/9/20

class Stack (object):

    def __init__(self):
        self.stack = []

    # add an item to the top of the stack
    def push(self, item):
        self.stack.append(item)

    # remove an item from the top of the stack
    def pop(self):
        return self.stack.pop()

    # check the item on the top of the stack
    def peek(self):
        return self.stack[-1]

    # check if the stack if empty
    def is_empty(self):
        return (len(self.stack) == 0)

    # return the number of elements in the stack
    def size(self):
        return (len(self.stack))


class Vertex (object):

    def __init__(self, label):
        self.label = label
        self.visited = -1

    # determine if a vertex was visited
    def was_visited(self):
        return self.visited

    # determine the label of the vertex
    def get_label(self):
        return self.label

    # string representation of the vertex
    def __str__(self):
        return str(self.label)


class Graph (object):

    def __init__(self):
        self.Vertices = []
        self.adjMat = []
        self.toposortlist = []

    # determine if a directed graph has a cycle
    # this function should return a boolean and not print the result
    def has_cycle(self):

        # create the Stack
        theStack = Stack()

        # mark the vertex v as visited and push it on the Stack
        (self.Vertices[0]).visited = 0
        theStack.push(0)

        # visit all the other vertices according to depth
        while (not theStack.is_empty()):
            # get an adjacent unvisited vertex
            u = self.get_adj_unvisited_vertex(theStack.peek())
            if (u == -1):
                u = theStack.pop()
                self.Vertices[u].visited = 1
            else:
                if self.Vertices[u].visited == 0:
                    return True
                self.Vertices[u].visited = 0
                theStack.push(u)

        # the stack is empty, let us rest the flags
        nVert = len(self.Vertices)
        for i in range(nVert):
            (self.Vertices[i]).visited = -1
        return False

    # return a list of vertices after a topological sort
    # this function should not print the list
    def toposort(self):

        if self.has_cycle() == True:
            return

        n = len(self.Vertices)

        while n > 0:
            vert = -1
            for col in range(n):
                sum = 0
                for row in range(n):
                    sum += self.adjMat[row][col]
                if sum == 0:
                    vert = col
                    label = self.Vertices[vert].get_label()
                    self.toposortlist.append(label)
                    self.delete_vertex(label)
                    n -= 1
                    break

        return self.toposortlist

    # check if a vertex is already in the graph
    def has_vertex(self, label):
        nVert = len(self.Vertices)
        for i in range(nVert):
            if label == self.Vertices[i].get_label():
                return True
        return False

    # get the index from the vertex label
    def get_index(self, label):

        nVert = len(self.Vertices)
        for i in range(nVert):
            if label == self.Vertices[i].get_label():
                return i
        return -1

    # add a Vertex object with a given label to the graph
    def add_vertex(self, label):

        if (not self.has_vertex(label)):
            self.Vertices.append(Vertex(label))

        # add a new column in the adjacency matrix
        nVert = len(self.Vertices)
        for i in range(nVert - 1):
            (self.adjMat[i]).append(0)

        # add a new row for the new vertex
        new_row = []
        for i in range(nVert):
            new_row.append(0)
        self.adjMat.append(new_row)

    # add weighted directed edge to graph
    def add_directed_edge(self, start, finish, weight=1):
        self.adjMat[start][finish] = weight

    def get_adj_unvisited_vertex(self, v):

        nVert = len(self.Vertices)
        for i in range(nVert):
            if self.adjMat[v][i] > 0 and self.Vertices[i].was_visited() != 1:
                return i
        return -1

    def delete_vertex(self, vertexLabel):

        index = self.get_index(vertexLabel)

        if index == -1:
            return

        n = len(self.Vertices)
        for i in range(n):
            self.adjMat[i].pop(index)

        self.adjMat.pop(index)

        for i in range(n):
            if self.Vertices[i].get_label() == vertexLabel:
                self.Vertices.pop(i)
                break


def main():
    # create a Graph object
    theGraph = Graph()
    in_file = open("topo.txt", "r")

    # Get num vertices
    num_vertices = int(in_file.readline().strip())
    for vert in range(num_vertices):
        theGraph.add_vertex(in_file.readline().strip())

    # Get num edges
    num_edges = int(in_file.readline().strip())
    for edge in range(num_edges):
        edge_to_edge = in_file.readline().strip()
        start = theGraph.get_index(edge_to_edge[0])
        finish = theGraph.get_index(edge_to_edge[-1])
        theGraph.add_directed_edge(start, finish)

    # test if a directed graph has a cycle
    if (theGraph.has_cycle()):
        print("The Graph has a cycle.")
    else:
        print("The Graph does not have a cycle.")

    # test topological sort
    if (not theGraph.has_cycle()):
        vertex_list = theGraph.toposort()
        print("\nList of vertices after toposort")
        print(vertex_list)


main()
