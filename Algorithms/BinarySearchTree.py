class BST:
    def __init__(self, valueOfNode):
        self.value = valueOfNode
        self.left = None
        self.right = None

    def insert(self, value):
        node = self
        parent = None

        while node is not None:
            if node.value <= value:
                if node.right is None:
                    node.right = BST(value)
                    break
                else:
                    node = node.right

            else:
                if node.left is None:
                    node.left = BST(value)
                    break
                else:
                    node = node.left
        return self

    def contains(self, value):
        returnValue = False
        node = self

        while node is not None:
            if node.value < value:
                node = node.right
            elif node.value > value:
                node = node.left
            else:
                returnValue = True
                return returnValue
        return returnValue



    def remove(self, value):
        #first need to find 'value' in BST
        node = self
        parent = None
        whichChild = ""

        while node is not None:
            if node.value < value:
                parent = node
                whichChild = "right"
                node = node.right
            elif node.value > value:
                parent = node
                whichChild = "left"
                node = node.left
            else: #if we are here, we have found our 'value'!
                break
        if node is None: #This means that the 'value' was not found in the BST. There is nothing to delete
            return self
        else:
            # case 1 : node is a leaf. This can be simply deleted
            if node.left is None and node.right is None:
                if whichChild == "right":
                    parent.right = None
                if whichChild == "left":
                    parent.left = None
            # case 2: node has only one child. The child of this node should be the new child of the parent of the node
            elif node.left is None and node.right is not None:
                parent.right = node.right
            elif node.left is not None and node.right is None:
                parent.left = node.left
            # case 3: node has two children. We need to find the maximal value in the left subtree and replace deleted node with this. This maximal node can only have a left child, which is case 2 again
            else:
                maximalNode = node.left
                maximalNodeParent = node
                while maximalNode.right is not None:
                    naximalNodeParent = maximalNode
                    maximalNode = maximalNode.right

                if maximalNode.left is not None:
                    maximalNodeParent.right = maximalNode.left

                node.value = maximalNode.value



            return self





