#  File: GraphTraversal.py
#  Description: HW 16
#  Student Name: Alice Liang
#  Student UT EID: axl84
#  Course Name: CS 313E
#  Unique Number: 84825
#  Date Created: 08/5/20
#  Date Last Modified: 08/7/20

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


class Queue (object):
    def __init__(self):
        self.queue = []

    # add an item to the end of the queue
    def enqueue(self, item):
        self.queue.append(item)

    # remove an item from the beginning of the queue
    def dequeue(self):
        return (self.queue.pop(0))

    # check if the queue is empty
    def is_empty(self):
        return (len(self.queue) == 0)

    # return the size of the queue
    def size(self):
        return (len(self.queue))


class Vertex (object):

    def __init__(self, label):
        self.label = label
        self.visited = False

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

    # add weighted undirected edge to graph
    def add_undirected_edge(self, start, finish, weight=1):
        self.adjMat[start][finish] = weight
        self.adjMat[finish][start] = weight

    # get edge weight between two vertices
    # return -1 if edge does not exist
    def get_edge_weight(self, fromVertexLabel, toVertexLabel):

        rowIndex = self.get_index(fromVertexLabel)
        colIndex = self.get_index(toVertexLabel)

        weight = self.adjMat[rowIndex][colIndex]
        if weight != 0:
            return weight
        return -1

    # get a list of immediate neighbors that you can go to from a vertex
    # return a list of indices or an empty list if there are none
    def get_neighbors(self, vertexLabel):

        index = self.get_index(vertexLabel)
        neighborList = []

        n = len(self.Vertices)
        for i in range(n):
            if self.adjMat[index][i] > 0:
                neighborList.append(i)

        return neighborList

    def get_adjacent_matrix(self):

        adjMatrixStr = ''
        n = len(self.Vertices)

        for i in range(n):
            row = ''
            for j in range(n):
                row += str(self.adjMat[i][j])
                row += ' '
            row.strip()
            row += '\n'
            adjMatrixStr += row

        return adjMatrixStr

    # return an index to an unvisited vertex adjacent to vertex v (index)
    def get_adj_unvisited_vertex(self, v):

        nVert = len(self.Vertices)
        for i in range(nVert):
            if (self.adjMat[v][i] > 0) and (not (self.Vertices[i]).was_visited()):
                return i
        return -1

    def get_all_adj_unvisited_vertex(self, v):

        adjVertexList = []
        nVert = len(self.Vertices)
        for i in range(nVert):
            if (self.adjMat[v][i] > 0) and (not (self.Vertices[i]).was_visited()):
                adjVertexList.append(i)
        return adjVertexList

    # get a copy of the list of Vertex objects
    def get_vertices(self):

        vertexObjList = []

        n = len(self.Vertices)
        for i in range(n):
            original = self.Vertices[i]
            vertexObject = Vertex(original.label)
            vertexObjList.append(vertexObject)

        return vertexObjList

    def get_cities(self):

        vertexStr = ''
        n = len(self.Vertices)

        for i in range(n):
            vertexStr += self.Vertices[i].get_label() + '\n'

        return vertexStr

    # do a depth first search in a graph starting at vertex v (index)
    def dfs(self, v):

        # create the Stack
        theStack = Stack()

        # mark the vertex v as visited and push it on the Stack
        (self.Vertices[v]).visited = True
        print(self.Vertices[v])
        theStack.push(v)

        # visit all the other vertices according to depth
        while (not theStack.is_empty()):
            # get an adjacent unvisited vertex
            u = self.get_adj_unvisited_vertex(theStack.peek())
            if (u == -1):
                u = theStack.pop()
            else:
                (self.Vertices[u]).visited = True
                print(self.Vertices[u])
                theStack.push(u)

        # the stack is empty, let us rest the flags
        nVert = len(self.Vertices)
        for i in range(nVert):
            (self.Vertices[i]).visited = False

    # do a breadth first search in a graph starting at vertex v (index)
    def bfs(self, v):

        # create the Queue
        theQueue = Queue()

        # mark the vertex v as visited and push it on the Stack
        (self.Vertices[v]).visited = True
        # print (self.Vertices[v])
        theQueue.enqueue(v)

        # visit all the other vertices according to depth
        while (not theQueue.is_empty()):
            # get an adjacent unvisited vertex
            u = theQueue.dequeue()

            if (u == -1):
                u = theQueue.dequeue()
            else:
                print(self.Vertices[u])

            lst = self.get_all_adj_unvisited_vertex(u)
            for i in range(len(lst)):
                vert = lst[i]
                self.Vertices[vert].visited = True
                theQueue.enqueue(vert)

        # the stack is empty, let us rest the flags
        nVert = len(self.Vertices)
        for i in range(nVert):
            (self.Vertices[i]).visited = False

    # delete an edge from the adjacency matrix
    # delete the edge if the graph is going from start to finish
    def delete_edge(self, fromVertexLabel, toVertexLabel):

        rowIndex = self.get_index(fromVertexLabel)
        colIndex = self.get_index(toVertexLabel)

        if rowIndex > -1 and colIndex > -1:
            # if self.adjMat[rowIndex][colIndex] > 0 and self.adjMat[colIndex][rowIndex] > 0:
            self.adjMat[colIndex][rowIndex] = 0
            self.adjMat[rowIndex][colIndex] = 0

    # delete a vertex from the vertex list and all edges from and
    # to it in the adjacency matrix
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

    cities = Graph()
    in_file = open("graph1.txt", "r")

    num_vertices = int(in_file.readline().strip())

    # read all the Vertices and add them the Graph
    for i in range(num_vertices):
        city = in_file.readline().strip()
        cities.add_vertex(city)

    # read the number of edges
    num_edges = int(in_file.readline().strip())

    # read the edges and add them to the adjacency matrix
    for i in range(num_edges):
        edge = in_file.readline().strip()
        edge = edge.split()
        start = int(edge[0])
        finish = int(edge[1])
        weight = int(edge[2])

        cities.add_directed_edge(start, finish, weight)

    # read the starting vertex fro dfs and bfs
    start_vertex = in_file.readline().strip()

    # get the index of the starting vertex
    start_index = cities.get_index(start_vertex)

    # test depth first search
    print("\nDepth First Search")
    cities.dfs(start_index)

    # test breadth first search
    print("\nBreadth First Search ")
    cities.bfs(start_index)
    print()

    # test deletion of an edge
    print("Deletion of an edge")

    twoCities = in_file.readline().strip()
    city = twoCities.split()

    print("\nAdjacency Matrix")
    cities.delete_edge(city[0], city[1])
    delEdge = cities.get_adjacent_matrix()
    print(delEdge)

    # test deletion of a vertex
    delCity = in_file.readline().strip()
    cities.delete_vertex(delCity)

    print("Deletion of a vertex\n")
    print("List of Vertices")
    print(cities.get_cities())

    print("Adjacency Matrix")
    delVertex = cities.get_adjacent_matrix()
    print(delVertex)


if __name__ == "__main__":
    main()
