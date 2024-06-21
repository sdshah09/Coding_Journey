'''
Shortest Path in Directed Acyclic Graph
Last Updated : 03 Feb, 2023
Given a Weighted Directed Acyclic Graph and a source vertex in the graph, find the shortest paths from given source to all other vertices.

Recommended Problem
Shortest path from 1 to n
Mathematical
Graph
+3 more
Morgan Stanley
Accolite
+3 more
Solve Problem
Submission count: 80.9K
For a general weighted graph, we can calculate single source shortest distances in O(VE) time using Bellman–Ford Algorithm. For a graph with no negative weights, we can do better and calculate single source shortest distances in O(E + VLogV) time using Dijkstra’s algorithm. Can we do even better for Directed Acyclic Graph (DAG)? We can calculate single source shortest distances in O(V+E) time for DAGs. The idea is to use Topological Sorting.

We initialize distances to all vertices as infinite and distance to source as 0, then we find a topological sorting of the graph. Topological Sorting of a graph represents a linear ordering of the graph (See below, figure (b) is a linear representation of figure (a) ). Once we have topological order (or linear representation), we one by one process all vertices in topological order. For every vertex being processed, we update distances of its adjacent using distance of current vertex.


'''

'''
Steps

Algorithm
Topological Sort
Create a Stack (say st) which will be used to store the topological ordering.
Create a boolean array (say visited), it will be used to mark the vertices which have been visited.
For each unvisited vertex (say node) from 0 to V-1 call a recursive helper function which will do the following:
Mark node as visited.
For each adjacent vertex of node call the recursive function.
Push node in st.
Shortest Path
Find topological ordering of the given graph
Create an array (say dist) of size V, and initialize all its entries with a very large number (say INF).
Traverse over all the vertices in topological order and for each vertex u, check the following conditon for all the adjancent vetex v of u If ( dist[v] > dist[u] + weightOfEdge(u
→
→v)) then dist[v] =dist[u] + weightOfEdge(u
→
→v)

'''

from collections import defaultdict

class Node:
    def __init__(self,v,weight) -> None:
        self.v = v
        self.wt = weight
        
class Graph:
    
    def __init__(self,V) -> None:
        self.adj = defaultdict(list)
        self.V = V
    def addEdge(self,u,v,wt):
        self.adj[u].append(Node(v,wt))
        
    def dfs(self,node,visited,res): # Topological Sort
        visited[node] = True
        for vertex in self.adj[node]:
            if not visited[vertex.v]:
                self.dfs(vertex.v,visited,res)
            
        res.append(node)
        # print(res)
    def shortestPath(self,src,V): # Shorted Path in which create an array of ditance which will keep the track of distance from every node to source in an array and return it. If the node is unreachable then it will print infinity for it
        st = []
        dist = [float('inf')]*self.V
        dist[src] = 0
        visited = [False]*self.V
        
        for i in range(V):
            if not visited[i]:
                self.dfs(i,visited,st)
        while len(st)>0:
            u = st.pop()
            if dist[u]!=float('inf'):
                for node in self.adj[u]:
                    if dist[node.v]>dist[u]+node.wt:
                        dist[node.v] = dist[u] + node.wt
                        
        for i in range(V):
            if dist[i]==float('inf'):
                print("INF"),
            else:
                print(dist[i]),

V=6    
g=Graph(V)
# Add edges.
g.addEdge(0, 2, 4)
g.addEdge(1, 0, 3)
g.addEdge(2, 3,-3)
g.addEdge(2, 4, 2)
g.addEdge(1, 2, 2)
g.addEdge(1, 3, 5)
g.addEdge(4, 3, 2)

# Find the shortest path from a 
# vertex (here 0).
g.shortestPath(0,V)

    