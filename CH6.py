# GRAPHS (Data Structure)

# Breadth first seach - solve the shortest-path problem
# Steps:
# 1. Model the problem as a graph.
# 2. Solve the problem using breadth-first search.
#
# Breadth-first search takes O(number of people + number of edges)
# - O(V+E) (V for number of vertices, E for number of edges).

# Graphs: models a set of connections
#         made up of nodes and edges
# • Question type 1: Is there a path from node A to node B?
# • Question type 2: What is the shortest path from node A to node B?

# A hash table is a data structure that lets you express relationships
# in graphs.
# Remember, a hash table allows you to map a key to a
# value. In this case, you want to map a node to all of its
# neighbors.

from collections import deque

graph = {}
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anum", "peggy"]
graph["anum"] = []
graph["peggy"] = []
graph["alice"] = []
graph["claire"] = []

def person_is_seller(name):
    return name[-1] == "m"

def queue_mango():
    search_queue = deque()
    search_queue += graph["you"]

    while search_queue:
        person = search_queue.popleft()
        if person_is_seller(person):
            print(person + " is a mango seller!")
            return True
        else:
            search_queue += graph[person]
            return False

def search(name):
    search_queue = deque()
    search_queue += graph[name]
    searched = []
    while search_queue:
        person = search_queue.popleft()

        if not person in searched:
            if person_is_seller(person):
                print(person + " is a mango seller!")
                return True
            else:
                search_queue += graph[person]
                searched.append(person)
    return False

print(search("you"))

# directed graph — the relationship is only one way, arrow pointers


# Queues (Data Structure)

# Queues are similar to stacks
# only 2 operations, enqueue and dequeue
# enqueue - add item at the end of list
# dequeue - take off item from front of list

# queue is called a FIFO data structure: First In, First Out
# stack is called a LIFO data structure: Last In, First Out

# Topological sort

# a way to make an ordered list out of a graph
# Where task A depends on task B and comes later on

# Tree - a special type of graph, where no edges ever point back.
