# **Problem1-Leetcode#200-Number of Islands-Medium**

# Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

 

# - Example 1:

# Input: grid = [\
#   ["1","1","1","1","0"],\
#   ["1","1","0","1","0"],\
#   ["1","1","0","0","0"],\
#   ["0","0","0","0","0"]\
# ]

# Output: 1

# - Constraints:

#     - m == grid.length
#     - n == grid[i].length

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0
        
        islands = 0
        visit = set()
        rows, cols = len(grid), len(grid[0])
        
        def dfs(r, c):
            if (r < 0 or r >= rows or c < 0 or c >= cols or
                grid[r][c] == '0' or (r, c) in visit):
                return
            visit.add((r, c))
            directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
            for dr, dc in directions:
                dfs(r + dr, c + dc)
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1' and (r, c) not in visit:
                    islands += 1
                    dfs(r, c)
        
        return islands
