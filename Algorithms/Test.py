
from collections import deque


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