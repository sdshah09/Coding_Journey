'''
Shortest Cell Path
In a given grid of 0s and 1s, we have some starting row and column sr, sc and a target row and column tr, tc. Return the length of the shortest path from sr, sc to tr, tc that walks along 1 values only.

Each location in the path, including the start and the end, must be a 1. Each subsequent location in the path must be 4-directionally adjacent to the previous location.

It is guaranteed that grid[sr][sc] = grid[tr][tc] = 1, and the starting and target positions are different.

If the task is impossible, return -1.

Examples:

input:
grid = [[1, 1, 1, 1], [0, 0, 0, 1], [1, 1, 1, 1]]
sr = 0, sc = 0, tr = 2, tc = 0
output: 8
(The lines below represent this grid:)
1111
0001
1111

grid = [[1, 1, 1, 1], [0, 0, 0, 1], [1, 0, 1, 1]]
sr = 0, sc = 0, tr = 2, tc = 0
output: -1
(The lines below represent this grid:)
1111
0001
1011
Constraints:

[time limit] 5000ms
[input] array.array.integer grid
1 ≤ arr.length = arr[i].length ≤ 10
[input] integer sr
[input] integer sc
[input] integer tr
[input] integer tc
All sr, sc, tr, tc are valid locations in the grid, grid[sr][sc] = grid[tr][tc] = 1, and (sr, sc) != (tr, tc).
[output] integer

'''

from collections import deque

def shortestCellPath(grid, sr, sc, tr, tc):
    R = len(grid)
    C = len(grid[0]) if R > 0 else 0
    
    if not (0 <= sr < R and 0 <= sc < C and 0 <= tr < R and 0 <= tc < C):
        return -1
    
    queue = deque()
    queue.append((sr, sc, 0))
    seen = set()
    seen.add((sr, sc))
    
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right
    
    while queue:
        r, c, depth = queue.popleft()
        
        if r == tr and c == tc:
            return depth
        
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            
            if 0 <= nr < R and 0 <= nc < C and grid[nr][nc] == 1 and (nr, nc) not in seen:
                queue.append((nr, nc, depth + 1))
                seen.add((nr, nc))
    
    return -1
