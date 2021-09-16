# DIJKSTRA

# Weighted Graphs - Graphs where each edge has a weight on them.
# Dijkstra's algorithm finds the shortest path on weighted graphs.

# steps: 1. Find the “cheapest” node
#        2. Update the costs of the neighbors of this node
#        3. Repeat until you’ve done this for every node
#        4. Calculate the final path
#           - Go backwards, from finish to start of path

# directed acyclic graphs - a directed graph with no cycles
# Dijkstra's algorithm can only work with DAGs

# negative weight edges - edges with minus weight
# Dijkstra's algorithm can't run with negative weights,
# use Bellman-Ford algorithm instead.

graph = {}
graph["start"] = {}
graph["start"]["a"] = 6
graph["start"]["b"] = 2

graph["a"] = {}
graph["a"]["fin"] = 1

graph["b"] = {}
graph["b"]["a"] = 3
graph["b"]["fin"] = 5

graph["fin"] = {}


#     6   A    1
#      /  |  \
# START   3   FINISH
#      \  |  /
#     2   B    5


# COSTS
infinity = float("inf")
costs = {}
costs["a"] = 6
costs["b"] = 2
costs["fin"] = infinity

# PARENTS
parents = {}
parents["a"] = "start"
parents["b"] = "start"
parents["fin"] = None

processed = []

def find_lowest_cost_node(costs):
    lowest_cost = float("inf")
    lowest_cost_node = None
    for node in costs: 
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost 
            lowest_cost_node = node
    return lowest_cost_node

node = find_lowest_cost_node(costs)
while node is not None:
    cost = costs[node]
    neighbors = graph[node]
    for n in neighbors.keys():
        new_cost = cost + neighbors[n]
        if costs[n] > new_cost:
            costs[n] = new_cost
            parents[n] = node
    processed.append(node)
    node = find_lowest_cost_node(costs)