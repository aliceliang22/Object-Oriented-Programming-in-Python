#  File: ExpressionTree.py
#  Description: HW 14
#  Student Name: Alice Liang
#  Student UT EID: axl84
#  Course Name: CS 313E
#  Unique Number: 84825
#  Date Created: 07/30/20
#  Date Last Modified: 07/31/20

class Stack (object):

    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        return self.stack.pop()

    def peek(self):
        return self.stack[-1]

    def is_empty(self):
        return (len(self.stack) == 0)

    def size(self):
        return (len(self.stack))


class Node (object):

    def __init__(self, data=None):
        self.data = data
        self.lchild = None
        self.rchild = None


class Tree (object):

    def __init__(self):
        self.root = Node()
        self.stack = Stack()

    def create_tree(self, expr):

        tokens = expr.split()
        n = len(tokens)

        if n == 0:
            return

        currentNode = self.root

        for token in tokens:
            if token == "(":
                newNode = Node()
                currentNode.lchild = newNode
                self.stack.push(currentNode)
                currentNode = newNode

            elif self.isOperator(token) == True:
                currentNode.data = token
                self.stack.push(currentNode)
                newNode = Node()
                currentNode.rchild = newNode
                currentNode = newNode

            elif self.isOperand(token) == True:
                currentNode.data = token
                currentNode = self.stack.pop()

            elif token == ")":
                if self.stack.is_empty() == False:
                    currentNode = self.stack.pop()

    def evaluate(self, aNode):

        if aNode == None:
            return 0

        if aNode.lchild == None and aNode.rchild == None:
            # if aNode.data.isnumeric() == True:
            # return int(aNode.data)
            try:
                f = float(aNode.data)
                return f

            except ValueError:
                return 0

        leftVal = self.evaluate(aNode.lchild)

        rightVal = self.evaluate(aNode.rchild)

        if aNode.data == '+':
            return leftVal + rightVal

        elif aNode.data == '-':
            return leftVal - rightVal

        elif aNode.data == '*':
            return leftVal * rightVal

        elif aNode.data == '**':
            return leftVal ** rightVal

        elif aNode.data == '/':
            return leftVal / rightVal

        elif aNode.data == '//':
            return leftVal // rightVal

        elif aNode.data == '%':
            return leftVal % rightVal

        return 0

    def pre_order(self, aNode):

        if (aNode != None):
            result = aNode.data
            lResult = self.pre_order(aNode.lchild)
            rResult = self.pre_order(aNode.rchild)

            if len(lResult) > 0:
                result += " "
                result += lResult

            if len(rResult) > 0:
                result += " "
                result += rResult

            return result
        else:
            return ""

    def post_order(self, aNode):

        if (aNode != None):

            lResult = self.post_order(aNode.lchild)
            rResult = self.post_order(aNode.rchild)

            result = ''

            if len(lResult) > 0:
                result += lResult
                result += " "

            if len(rResult) > 0:
                result += rResult
                result += " "

            result += aNode.data
            return result

        else:
            return ""

    def isOperand(self, c):

        if len(c) == 0:
            return False

        if c.isnumeric() == True:
            return True
        try:
            float(c)
            return True
        except ValueError:
            return False

        return False

    def isOperator(self, op):

        if op == '+':
            return True
        if op == '-':
            return True
        if op == '*':
            return True
        if op == '/':
            return True
        if op == '%':
            return True
        if op == '//':
            return True
        if op == '**':
            return True

        return False


def main():

    expr = "( ( ( 8 / 2 ) ** ( 7 % 2 ) ) * 6.2 )"

    tree = Tree()
    tree.create_tree(expr)
    evaluate = tree.evaluate(tree.root)
    print(evaluate)

    tree.pre_order(tree.root)
    print("post")
    tree.post_order(tree.root)


main()
