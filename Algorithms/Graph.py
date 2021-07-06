# Now just a static function to generate the graph as described in the Algorithms book. LATER : make a class to generate these datastructs

def generateGraph():
    graph = {}
    graph["start"] = {}
    graph["start"]["a"] = 6
    graph["start"]["b"] = 2
    graph["a"] = {}
    graph["a"]["fin"] = 1
    graph["b"] = {}
    graph["b"]["fin"] = 5
    graph["b"]["a"] = 3
    graph["fin"] = {}
    return  graph
