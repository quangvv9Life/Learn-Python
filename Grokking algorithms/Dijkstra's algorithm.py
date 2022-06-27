# hash table stores the neighbors and the cost for getting to that neighbor
graph = {}
# Start has two neighbors, A and B
graph["start"]      = {}
graph["start"]["a"] = 6
graph["start"]["b"] = 2

graph["a"]        = {}
graph["a"]["fin"] = 1 # A has one neighbor, Fin

graph["b"]        = {}
graph["b"]["a"]   = 3
graph["b"]["fin"] = 5

graph["fin"] = {}

print(graph)
# the cost of a node is how long it takes to get to that node from the start
# hash table for costs
infinity = float("inf")
costs = {}
costs["a"]   = 6
costs["b"]   = 2
costs["fin"] = infinity

print(cost)
# hash table for the parents
parents = {}
parents["a"]     = "start"
parents["b"]     = "start"
parents["fin"]   = None

print(parents)
# this is to keep track of all the nodes you've already processed
processed = []

# find the lowest cose node that you haven't processed yet
def find_lowest_cost_node(costs):
    lowest_cost     = float("inf")
    lowst_cost_node = None
    # go through each node
    for node in costs:
        cost = costs[node]
        # if it's the lowest cost so far and hasn't been processed yet...
        if cost < lowest_cost and node not in processed:
            lowest_cost     = cost #... set it as the new lowest-cost node
            lowst_cost_node = node
    return lowst_cost_node

node = find_lowest_cost_node(costs)
# if you've processed all the nodes, this while loop is done
while node is not None:
    cost      = costs[node]
    neighbors = graph[node]
    # go through all the neighbors of this node
    for n in neighbors.keys():
        new_cost = cost + neighbors[n]
        # if it's cheaper to get to this neighbor by going through this node ...
        if costs[n] > new_cost:
            costs[n]   = new_cost # ...update the cost for this node
            parents[n] = node # this node becomes the new parent for this neighbor
    processed.append(node) # mark the node as processed
    node = find_lowest_cost_node(costs)