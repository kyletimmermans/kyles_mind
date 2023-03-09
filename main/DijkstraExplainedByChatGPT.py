import sys

# function to find the vertex with minimum distance value
def min_distance(dist, visited, V):
    # initialize minimum distance for next node
    min_dist = sys.maxsize
    # iterate over all vertices
    for v in range(V):
        # if the vertex hasn't been visited and the distance is less than the minimum distance
        if not visited[v] and dist[v] < min_dist:
            # set the minimum distance to the current distance and update the vertex
            min_dist = dist[v]
            min_index = v
    return min_index

# function to print the shortest path from source to destination
def print_path(parent, j):
    # base case
    if parent[j] == -1:
        print(j, end=' ')
        return
    # recursive call to print the path from source to parent of current vertex
    print_path(parent, parent[j])
    # print current vertex
    print(j, end=' ')

# function to print the distance of each vertex from the source vertex
def print_solution(dist, parent, src):
    print("Vertex \t Distance from Source \t Path")
    # iterate over all vertices except the source vertex
    for i in range(1, len(dist)):
        print(f"{src} -> {i} \t\t {dist[i]} \t\t\t\t", end=' ')
        # print the path from source to current vertex
        print_path(parent, i)
        print()

# function to implement Dijkstra's Algorithm
def dijkstra(graph, src, V):
    # initialize distances of all vertices as infinity and source vertex as 0
    dist = [sys.maxsize] * V
    dist[src] = 0
    # initialize visited list and parent list
    visited = [False] * V
    parent = [-1] * V
    # iterate over all vertices
    for _ in range(V):
        # find the vertex with minimum distance value from the set of vertices not yet processed
        u = min_distance(dist, visited, V)
        # mark the current vertex as visited
        visited[u] = True
        # update distance value of adjacent vertices if they haven't been visited and their distance is greater than the new distance
        for v in range(V):
            if graph[u][v] and not visited[v] and dist[v] > dist[u] + graph[u][v]:
                dist[v] = dist[u] + graph[u][v]
                parent[v] = u
    # print the solution
    print_solution(dist, parent, src)

# example adjacency matrix
graph = [[0, 2, 0, 6, 0],
         [2, 0, 3, 8, 5],
         [0, 3, 0, 0, 7],
         [6, 8, 0, 0, 9],
         [0, 5, 7, 9, 0]]
# number of vertices
V = len(graph)
# source vertex
src = 0
# run Dijkstra's Algorithm
dijkstra(graph, src, V)

