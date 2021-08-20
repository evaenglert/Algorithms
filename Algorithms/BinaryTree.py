from collections import deque


class BinaryTree:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value


# Implementation of traversals

# Inorder Tree Traversal: visiting left subtree, then node, then right subtree
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

# Preorder Tree Traversal: visiting root, left subtree, then right subtree
def preorder_recursive(root, array):
    node = root
    if node is None:
        return

    array.append(node.value)
    preorder_recursive(root.left, array)
    preorder_recursive(root.right, array)

def preorder_iterative(root):
    callStack = deque()
    array = []

    callStack.append(root)

    while len(callStack) != 0:
        currentNode = callStack.pop()

        if currentNode is None:
            return

        array.append(currentNode.value)

        if currentNode.right is not None:
            callStack.append(currentNode.right)
        if currentNode.left is not None:
            callStack.append(currentNode.left)

    return array