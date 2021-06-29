#  File: BinaryTrees.py
#  Description: HW 15
#  Student Name: Alice Liang
#  Student UT EID: axl84
#  Course Name: CS 313E
#  Unique Number: 84825
#  Date Created: 08/1/20
#  Date Last Modified: 08/3/20

class Node (object):
    def __init__(self, data):
        self.data = data
        self.lchild = None
        self.rchild = None


class Tree (object):
    def __init__(self):
        self.root = None

  # insert data into the tree
    def insert(self, data):

        new_node = Node(data)

        if (self.root == None):
            self.root = new_node
            return
        else:
            current = self.root
            parent = self.root

            while (current != None):
                parent = current
                if (data < current.data):
                    current = current.lchild
                else:
                    current = current.rchild

            # found location now insert node
            if (data < parent.data):
                parent.lchild = new_node
            else:
                parent.rchild = new_node

    # Returns true if two binary trees are similar
    def is_similar(self, pNode):

        if pNode == None:
            return False

        return areSimilar(self.root, pNode)

    # Prints out all nodes at the given level
    def print_level(self, level):

        return printNumLevel(self.root, level) + "\n"

    # Returns the height of the tree
    def get_height(self):

        return getTreeHeight(self.root)

    # Returns the number of nodes in tree which is equivalent to 1 + number of nodes in the left
    # subtree + number of nodes in the right subtree
    def num_nodes(self):

        return getNumNodes(self.root)


def areSimilar(a, b):

    if a == None and b == None:
        return True

    if a == None or b == None:
        return False

    if a.data != b.data:
        return False

    if areSimilar(a.lchild, b.lchild) == False:
        return False

    if areSimilar(a.rchild, b.rchild) == False:
        return False

    return True


def printNumLevel(root, num):

    if root == None:
        return ''

    if num < 0:
        return ''

    if num == 0:
        return str(root.data)

    else:
        left = printNumLevel(root.lchild, num - 1)
        right = printNumLevel(root.rchild, num - 1)
        if len(left) == 0 and len(right) == 0:
            return ''
        if len(left) == 0:
            return right
        if len(right) == 0:
            return left
        tmpstr = left + ' ' + right
        return tmpstr


def getTreeHeight(node):

    if node == None:
        return -1

    else:
        left = getTreeHeight(node.lchild)
        right = getTreeHeight(node.rchild)

        if (left > right):
            return left + 1
        else:
            return right + 1


def getNumNodes(node):

    if node == None:
        return 0

    else:
        left = getNumNodes(node.lchild)
        right = getNumNodes(node.rchild)
        return 1 + left + right


def main():

    tree1 = Tree()
    tree2 = Tree()

    tree1.insert(14)
    tree1.insert(17)
    tree1.insert(1)
    tree1.insert(3)
    tree1.insert(18)
    tree1.insert(21)

    tree2.insert(14)
    tree2.insert(17)
    tree2.insert(1)
    tree2.insert(3)
    tree2.insert(18)
    tree2.insert(21)

    if tree1.is_similar(tree2.root):
        print("Trees are similar")
    else:
        print("Trees are different")

    level = 3
    tree1.print_level(level)
    print()

    height = tree1.get_height()
    print(height)

    numNodes = tree1.num_nodes()
    print(numNodes)


if __name__ == '__main__':
    main()
