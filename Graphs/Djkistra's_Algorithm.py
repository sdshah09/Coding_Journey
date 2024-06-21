'''
Dijkstra’s Shortest Path Algorithm using priority_queue of STL
Last Updated : 28 Mar, 2024
Given a graph and a source vertex in graph, find shortest paths from source to all vertices in the given graph.

Input : Source = 0
Output : 
     Vertex   Distance from Source
        0                0
        1                4
        2                12
        3                19
        4                21
        5                11
        6                9
        7                8
        8                14

1) Initialize distances of all vertices as infinite.
2) Create an empty priority_queue pq.  Every item
   of pq is a pair (weight, vertex). Weight (or 
   distance) is used  as first item  of pair
   as first item is by default used to compare
   two pairs
3) Insert source vertex into pq and make its
   distance as 0.
4) While either pq doesn't become empty
    a) Extract minimum distance vertex from pq. 
       Let the extracted vertex be u.
    b) Loop through all adjacent of u and do 
       following for every vertex v.
           // If there is a shorter path to v
           // through u. 
           If dist[v] > dist[u] + weight(u, v)
               (i) Update distance of v, i.e., do
                     dist[v] = dist[u] + weight(u, v)
               (ii) Insert v into the pq (Even if v is
                    already there)
               
5) Print distance array dist[] to print all shortest
   paths. 

'''

import heapq

class Graph:
    def __init__(self,V) -> None:
        self.V =V
        self.adj = [[] for _ in range(V)]
    def addEdge(self,u,v,wt):
        self.adj[u].append((v,wt))
        self.adj[v].append((u,wt))
        
    def shortestPath(self,src):
        minHeap = [(0,src)]
        dist = [float('inf')]*self.V
        dist[src] = 0
        while minHeap:
            currentDis,u = heapq.heappop(minHeap)
            
            for v,weight in self.adj[u]:
                if dist[v]>dist[u]+weight:
                    dist[v] = dist[u] + weight
                    heapq.heappush(minHeap,(dist[v],v))
        print("Vertex Distance from Source")
        for i in range(self.V):
            print(f"{i}\t\t{dist[i]}")
if __name__ == "__main__":
    # Create the graph given in the above figure
    V = 9
    g = Graph(V)

    # Making the above-shown graph
    g.addEdge(0, 1, 4)
    g.addEdge(0, 7, 8)
    g.addEdge(1, 2, 8)
    g.addEdge(1, 7, 11)
    g.addEdge(2, 3, 7)
    g.addEdge(2, 8, 2)
    g.addEdge(2, 5, 4)
    g.addEdge(3, 4, 9)
    g.addEdge(3, 5, 14)
    g.addEdge(4, 5, 10)
    g.addEdge(5, 6, 2)
    g.addEdge(6, 7, 1)
    g.addEdge(6, 8, 6)
    g.addEdge(7, 8, 7)

    g.shortestPath(0)
