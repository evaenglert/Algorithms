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

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hello  there, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    root = BST(10)
    root.left = BST(5)
    root.left.left = BST(2)
    root.left.left.left = BST(1)
    root.left.right = BST(5)
    root.right = BST(15)
    root.right.left = BST(13)
    root.right.left.right = BST(14)
    root.right.right = BST(22)

    print(root.remove(1))



