'''
200. Number of Islands

Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Accepted
2.7M
Submissions
4.6M
Acceptance Rate
59.6%
 

Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 300
grid[i][j] is '0' or '1'.

'''
from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        self.count = 0
        self.grid = grid
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    self.count += 1
                    self.dfs(grid, i, j)
        
        return self.count
    
    def dfs(self, grid, m, n):
        if m < 0 or n < 0 or m >= len(grid) or n >= len(grid[0]) or grid[m][n] != '1':
            return
        print(grid)
        grid[m][n] = '0' # Visited
        self.dfs(grid, m + 1, n)
        self.dfs(grid, m - 1, n)
        self.dfs(grid, m, n + 1)
        self.dfs(grid, m, n - 1)
if __name__ == "__main__":
    sol = Solution()
    print(sol.numIslands([
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]))