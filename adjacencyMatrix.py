'''
An adjacency matrix is a graph data structure that represents a weighted undirected graph.
It is an array of arrays in which all the arrays represent all of the nodes in a graph.
Each array is the size of how many nodes there are in the graph, so we know how far it is
from each node, to every other node.

Note: Values of 0 indicate no connection or connection to itself
'''

# Below is an example of an adjacency matrix data structure

adjacencyMatrix = [[0, 3, 4],   # Node 0
		   [3, 0, 2],   # Node 1
		   [4, 2, 0]]	# Node 2

# E.g. Node 2's row can be read iteratively as:
# Node 2 to Node 0 is 4, Node 2 to Node 1 is 2, Node 2 to Node 2 is 0

# The graph below represents the adjacency matrix above

'''

	    1
	   / \
	3 /   \ 2
	 /     \
	0-------2
	    4

'''

'''
adjacencyMatrix[x][y] = z

x is the row or source node
y is the destination node that x or the source node connects to
z is the weight of the edge between x and y
'''

# E.g. if we wanted the weight of the edge (z) between node 0 and node 2
print(adjacecyMatrix[0][2])  # This will return 4

'''
Logic for getting edge weights or connections:
Row Number (Source Node) --> Index (Destination Node) --> Value (Edge Weight Between Them)
     |		               |			    | 		
     |		               |			    |
     |                         V 			    |
     V		     0    1    2   			    |
     0            [  0,   3,   4  ]			    |
			       ^			    |	
        		       |____________________________|

So if we want to see if there is a connection between node 1 and node 2,
we check at row 1 if there is a non-zero number at index 2 which is node 2.
There is a 4, so from node 0 to node 2, there is a connection with a weight of 4.
'''

'''
An adjacency matrix is a list of source nodes and their connections to other
nodes with a weights

	src [connection, connection, connection]
	src [connection, connection, connection]
	src [connection, connection, connection]
'''
