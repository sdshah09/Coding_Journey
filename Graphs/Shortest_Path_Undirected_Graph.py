'''
You are given an Undirected Graph having unit weight of the edges, find the shortest path from src to all the vertex and if it is unreachable to reach any vertex, then return -1 for that vertex.

Example1:

Input:
n = 9, m= 10
edges=[[0,1],[0,3],[3,4],[4,5],[5,6],[1,2],[2,6],[6,7],[7,8],[6,8]] 
src=0
Output:
0 1 2 1 2 3 3 4 4

'''

from collections import deque
from typing import List

class Solution:
    def shortestPath(self, edges: List[List[int]], N: int, M: int, src: int) -> List[int]:
        # Create adjacency list from given edges
        adj = [[] for _ in range(N)]
        
        for i in range(M):
            adj[edges[i][0]].append(edges[i][1])
            adj[edges[i][1]].append(edges[i][0])
        
        # Initialize distance array with maximum distance (infinity)
        dist = [float('inf')] * N
        
        # Queue for BFS
        q = deque()
        
        # Distance of source node from itself is 0
        dist[src] = 0
        q.append(src)
        
        # Perform BFS to find shortest path
        while q:
            node = q.popleft()
            
            for neighbor in adj[node]:
                # If the distance of current node + 1 is less than the current distance of adjacent node,
                # update distance and add adjacent node to queue
                if dist[node] + 1 < dist[neighbor]:
                    dist[neighbor] = dist[node] + 1
                    q.append(neighbor)
        
        # Convert infinity to -1 for nodes that are not reachable from the source
        for i in range(N):
            if dist[i] == float('inf'):
                dist[i] = -1
        
        return dist

# Example usage:
if __name__ == "__main__":
    sol = Solution()
    edges = [[0, 1], [0, 2], [1, 2], [1, 3]]
    N = 4
    M = 4
    src = 0
    result = sol.shortestPath(edges, N, M, src)
    print(result)  # Output: [0, 1, 1, 2]
