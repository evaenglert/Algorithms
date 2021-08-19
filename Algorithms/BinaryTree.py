from collections import deque

class BinaryTree:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

# Implementation of traversals

#Inorder Tree Traversal: visiting left subtree, then node, then right subtree
def inorder_recursive(graph, array):
    if graph is None:
        return
    inorder_recursive(graph.left, array)
    array.append(graph.value)
    inorder_recursive(graph.right, array)

def inorder_iterative(graph):
    callStack = deque()
    array = []
    currentNode = graph

    while len(callStack) != 0 or currentNode is not None:

        if currentNode is not None:
            callStack.append(currentNode)
            currentNode = currentNode.left
        else:
            currentNode = callStack.pop()
            array.append(currentNode.value)
            currentNode = currentNode.right


    return array
        




