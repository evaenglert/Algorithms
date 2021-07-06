# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from BinarySearch import binarySearch
from Sorting import selectionSort
import Recursive as rs
import Sorting as s
import GraphAlgorithms as ga
import Graph as g



def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    graph = g.generateGraph()

    print(ga.dijkstraAlgorithm(graph, "start", "fin"))
