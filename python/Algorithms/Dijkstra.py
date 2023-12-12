 # Shortest Path Problem 
 # Given weighted directed graph G(V, E)
 #  Dijkstra assumes that all edge weigths in the input graph are non negative
 # w(p) = S(u,v) // Shortest path from u to v 
 # along the shortest path <u , u_1, u_2 ... v>

 # w: E -> R // weigths are some real number
# Our shortest path is build on top of the assumption that our subpaths 
# are shortest paths 

# Negative edges can create cycles 
# I a non negative weighted edges graph
# We can assure to obtain the shortest path by removing O-weigth cycles
# and w(p') = w(p) - w(p) < w(p) // w(c) being a sub path that improves w(p) 




 
a = [
    [0,2,1,3,4,5],
    [5,4,0,3,5,6],
    [2,3,5,5,6],
    [3,5,2,5,3],
    [4,5,1],
    [1,2,4]
 ]

b = [
    [0,1],
    [2],
    [0,1,2]
    ]


def initializeSource():
   