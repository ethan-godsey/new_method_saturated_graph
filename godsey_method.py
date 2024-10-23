'''Author Ethan Godsey'''
import sys
from future import __annotations__

class Vertex:
    def __init__(self,num):
        self.id = num  #identifier
        self.adj = []  # list of adjacent vertices
        self.color = 'noColor'  # usefule to mark as visited

    # adds an adjacent vertex    
    def addNeighbor(self,nbr):
        self.adj.append(nbr)

    # deletes a vertex from adjacency list
    def delNeighbor(self, nbr):
        self.adj.remove(nbr)

    def __str__(self):
        return str(self.id) 

    # these are useful methods for managing vertex info
    def setColor(self,color):
        self.color = color
    def getColor(self):
        return self.color
    def getAdj(self):
        return self.adj
    def getId(self):
        return self.id

# this graph data structure is for unweighted, undirected graphs
# the connections are listed as part of each vertex (see above)
class Graph:
    def __init__(self):
        self.vertList = {}  # that's a dictionary, not a set
        self.numVertices = 0
        self.deletedVerts = {} # vertices we might want back, with connections
 
    def addVertex(self,key): # adds a vertex to the graph
        self.numVertices = self.numVertices + 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex
   
   # deleting a vertex also involves deleting all edges connecting to it
    def delVertex(self, key):
        self.numVertices = self.numVertices - 1
        current = self.vertList[key]
        for v in current.getAdj():
            v.delNeighbor(current)
 
        self.deletedVerts[key] = self.vertList.pop(key)

    def getVertex(self,n): # checks whether vertex 'n' is in the graph
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None

    def has_key(self,n):
        if n in self.vertList:
            return True
     
   # note this adds the edge both ways, so G is undirected
    def addEdge(self,f,t):
        if not f in self.vertList:
            nv = self.addVertex(f)
        if not t in self.vertList:
            nv = self.addVertex(t)
        self.vertList[f].addNeighbor(self.vertList[t])
        self.vertList[t].addNeighbor(self.vertList[f])	   

   # similarly we need to delete both ways.  Note vertices are not deleted
    def delEdge(self, f, t):
        self.vertList[f].delNeighbor(self.vertList[t])
        self.vertList[t].delNeighbor(self.vertList[f])

    def getVertices(self):
        return self.vertList.values()
        
    def __iter__(self):
        return self.vertList.itervalues()

P = Graph() 
for i in range(1,11):
    P.addVertex(i)
p = P.vertList[1]
P.addEdge(1,2)
P.addEdge(1,5)
P.addEdge(1,6)
P.addEdge(2,3)
P.addEdge(2,7)
P.addEdge(3,4)
P.addEdge(3,8)
P.addEdge(4,5)
P.addEdge(4,9)
P.addEdge(5,10)
P.addEdge(6,8)
P.addEdge(6,9)
P.addEdge(7,9)
P.addEdge(7,10)
P.addEdge(8,10)

# prism3 is the 3-prism graph
prism3 = Graph()
for i in range(1,7):
    prism3.addVertex(i)
prism3vert = prism3.vertList[1]
prism3.addEdge(1,2)
prism3.addEdge(1,3)
prism3.addEdge(1,5)
prism3.addEdge(2,3)
prism3.addEdge(2,6)
prism3.addEdge(3,4)
prism3.addEdge(4,5)
prism3.addEdge(4,6)
prism3.addEdge(5,6)


G = Graph()
for i in range(1,16):
    G.addVertex(i)
G.addEdge(1,2)
G.addEdge(1,3)
G.addEdge(1,4)
G.addEdge(2,3)
G.addEdge(2,5)
G.addEdge(3,4)
G.addEdge(4,5)
G.addEdge(5,6)
G.addEdge(6,7)
G.addEdge(6,12)
G.addEdge(7,8)
G.addEdge(7,10)
G.addEdge(8,9)
G.addEdge(8,11)
G.addEdge(9,10)
G.addEdge(9,11)
G.addEdge(10,11)
G.addEdge(12,13)
G.addEdge(12,15)
G.addEdge(13,14)
G.addEdge(13,16)
G.addEdge(14,15)
G.addEdge(14,16)
G.addEdge(15,16)


# N is a graph
N = Graph()
for i in range(1,11):
    N.addVertex(i)
n = N.vertList[1]
N.addEdge(1,6)
N.addEdge(1,9)
N.addEdge(1,10)
N.addEdge(2,10)
N.addEdge(3,4)
N.addEdge(4,6)
N.addEdge(4,8)
N.addEdge(4,10)
N.addEdge(5,10)
N.addEdge(6,7)
N.addEdge(6,9)

# B is a full, complete binary tree of height 3 with 15 vertices
B = Graph() 
for i in range(1,16):
    B.addVertex(i)
b = B.vertList[1]
B.addEdge(1,2)
B.addEdge(1,3)
B.addEdge(2,4)
B.addEdge(2,5)
B.addEdge(3,6)
B.addEdge(3,7)
B.addEdge(4,8)
B.addEdge(4,9)
B.addEdge(5,10)
B.addEdge(5,11)
B.addEdge(6,12)
B.addEdge(6,13)
B.addEdge(7,14)
B.addEdge(7,15)

NonBipartite = Graph()
for i in range(7):
    NonBipartite.addVertex(i)
NonBipartite.addEdge(1, 2)
NonBipartite.addEdge(2, 6)
NonBipartite.addEdge(6, 7)
NonBipartite.addEdge(7, 4)
NonBipartite.addEdge(7, 2)
NonBipartite.addEdge(6, 4)
NonBipartite.addEdge(3, 2)
NonBipartite.addEdge(3, 4)
NonBipartite.addEdge(4, 5)


def new_saturated_method(graph: Graph):
    max_saturation = []
    # find vertex with least degree
    
    #more than max possible degree
    degree = len(graph.vertList) + 1


    for vertex in graph.vertList:
        cur_degree = len(graph.vertList[vertex].adj)
        if cur_degree < degree and cur_degree != 0:
            degree = cur_degree

            #found our working vertex
            working_vertex = graph.vertList[vertex]

    
    # add edge for lowest degree neighbor, if multiple neighbors with same degree, pick lowest numbered vertex
    neighbor_degree = len(graph.vertList) + 1
    try:
        for neighbor in working_vertex.adj:
            if len(neighbor.adj) < neighbor_degree:
                lowest_deg = neighbor
    
    except UnboundLocalError:
        print(max_saturation)
        return max_saturation
        
    
    max_saturation.append('(' + str(working_vertex.id) + ',' + str(lowest_deg.id) + ')')

    # Remove 2 saturated verticies from viable verticies list, and decrease the degree of the neighbors by 1
    for vert in working_vertex.adj:
        for neighbor in vert.adj:
            if neighbor.id == working_vertex.id:
                vert.adj.remove(working_vertex)

    for vert in lowest_deg.adj:
        for neighbor in vert.adj:
            if neighbor.id == lowest_deg.id:
                vert.adj.remove(lowest_deg)

    del graph.vertList[working_vertex.id]
    del graph.vertList[lowest_deg.id]



    #repeat process for next lowest degreed vertex
    print(new_saturated_method(graph))
    print(max_saturation)

new_saturated_method(NonBipartite)
