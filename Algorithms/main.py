# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from BinarySearch import binarySearch
from Sorting import selectionSort
import Recursive as rs
import Sorting as s
import GraphAlgorithms as ga
import Graph as g
import GreedyAlgorithm as greedya
import DynamicProgramming as dp
from BinarySearchTree import BST
from BinaryTree import BinaryTree, inorder_recursive, inorder_iterative

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hello  there, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    root = BinaryTree(1)
    root.left = BinaryTree(2)
    root.right = BinaryTree(3)
    root.left.left = BinaryTree(4)
    root.right.left = BinaryTree(5)
    root.right.right = BinaryTree(6)
    root.right.left.left = BinaryTree(7)
    root.right.left.right = BinaryTree(8)
    array = []
    inorder_recursive(root, array)
    print(array)
    print(inorder_iterative(root))





