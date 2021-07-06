from collections import deque

def breadthFirstSearch(graph, firstToCheck, fnProperty):
    queue = deque()
    queue = queue + deque(graph[firstToCheck])

    while len(queue) != 0:
        personToCheck = queue.popleft()
        if fnProperty(personToCheck):
            return personToCheck;
            break
        else:
            queue = queue + deque(graph[personToCheck])


def dijkstraAlgorithm(graph, startVertex, endVertex):
    #hash table for costs:
    #hash table for costs need to include all vertices except the startVertex
    cost = {}
    parents = {}
    vertices = graph.keys()
    processed_node = []

    def find_lowest_cost_node(dict_cost, arr_processed_node, endVertex):
        not_processed = []
        minimal_cost = 100000000
        minimal_node = None
        for nodes in dict_cost.keys():
            if dict_cost[nodes] < minimal_cost and nodes not in arr_processed_node and nodes != endVertex:
                minimal_cost = dict_cost[nodes]
                minimal_node = nodes

        return minimal_node

    for vertex in vertices:
        if vertex in graph[startVertex]:
            cost[vertex] = graph[startVertex][vertex]
            parents[vertex] = startVertex
        elif vertex != startVertex:
            #this should be infinity...
            cost[vertex] = 10000000
            parents[vertex] = None

    node = find_lowest_cost_node(cost, processed_node, endVertex)
    while node is not None:

        for vertex in graph[node]:
            if cost[node] + graph[node][vertex] < cost[vertex]:
                cost[vertex] = cost[node] + graph[node][vertex]
                parents[vertex] = node
                processed_node.append(node)

        node = find_lowest_cost_node(cost, processed_node, endVertex)

    return cost











