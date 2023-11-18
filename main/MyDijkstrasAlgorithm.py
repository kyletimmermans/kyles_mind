'''
Dijkstra’s Algorithm
====================

Get all of the shortest paths and their distances from a given node
to all other nodes in a graph.

-Visit the shortest distanced unvisited node. During the beginning of the algorithm
this will be the src node (0 distance) while everyone else is still inf. After the 
1st step, this will then follow the smallest neighbor visited.

-Mark it as visited so we don't visit it again and calculate paths we've already searched.

-For the current node, visit all the neighbor node’s connected to it, if the distance
from the src to the current node + the distance it will take to get to the neighbor
from the currently selected node is less than the distance it currently takes to get
from the src node to get to said neighbor, update that neighbor’s distance to be the
distance it takes to get to the currently selected node + the distance it takes to get
to said neighbor. And also update said neighbor’s parent to be the currently selected
node as it represents the pointer to the fastest path

-Repeat

parent[] - point each node to its parent node that creates the shortest path. We can
follow child -> parent over and over again to create the lineage of shortest node connections

dist[] - Keep track of all the distances it took to get from src node to node x. When we add
the distance, we add what it took to get to the currently selected node, plus the distance it
takes to get from the current node to the neighbor. By adding what it took to get to the current
node plus what we’re about to add (distance to neighbor) we are storing everything from the past
and able to pass on everything from prior (entire path) to be used in the future. Sort of like
using the “+=“ operator and keeping track of the distances its taken to get to the current node,
without overwriting any progress, but rather adding on to it.

Both parent[] and dist[] are used to store the current best paths and their distances, and as we
move from smallest node to smallest node, we set nodes as visited (not visiting visited nodes) and
find new potential better paths and compare them against the current best options.
'''


infinity = float('inf')


# Recursively go from final destination (1st child) to src node (final parent)
# Child -> Parent -> Child -> Parent -> etc...
# Index -> Value -> Index -> Value -> etc...
def print_path(parent, j, spath):
    # base case
    if parent[j] == -1:
        spath.append(j)
        return
    print_path(parent, parent[j], spath)
    spath.append(j)


# For each node
#   For each of the nodes neighbors
def dijkstra(graph, src):
    V = len(graph)
    dist = [infinity] * V
    dist[src] = 0
    visited = [False] * V
    parent = [-1] * V

    # For all vertices
    for _ in range(V):

        # Find the shortest distanced non-visited vertex to work with
        temp_min = infinity
        min_idx = -1
        for v in range(V):
            if dist[v] < temp_min and not visited[v]:
                temp_min = dist[v]
                min_idx = v

        visited[min_idx] = True

        # For each of its neighbors, find the shortest path for src to said node
        for v in range(V):
            # If there's an edge between the two vertices and the destination is not visited
            if graph[min_idx][v] != 0 and not visited[v]:
                # Current + what we will add
                # If it doesn't beat previous shorter paths, don't add it
                if dist[min_idx] + graph[min_idx][v] < dist[v]:
                    # If its better, update the visited neighbors distance to be
                    # everything that was before the currently selected graph
                    # and the distance from there to the neighbor
                    dist[v] = dist[min_idx] + graph[min_idx][v]
                    # Update the neighbor's parent to be the currently selected node
                    # as its the node that comes just before it i.e. parent
                    parent[v] = min_idx


    # Print all shortest paths from src to every other node in the graph
    for i in range(len(graph)):
        # Path to itself
        if i == src:
            print(f"{src} to {src}: {src}")
            continue
        spath = []
        print_path(parent, i, spath)
        # Join path nodes with arrow
        print(f"{src} to {i}: {' -> '.join(map(str, spath))}")


# example adjacency matrix
# https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm#/media/File:Dijkstra_Animation.gif
graph = [[0, 7, 9, 0, 0, 14],  # 1
         [7, 0, 10, 15, 0, 0], # 2
         [9, 10, 0, 11, 0, 2], # 3
         [0, 15, 11, 0, 6, 0], # 4
         [0, 0, 0, 6, 0, 9],   # 5
         [14, 0, 2, 0, 9, 0]]  # 6

# source vertex
src = 0
# run Dijkstra's Algorithm
dijkstra(graph, src)
