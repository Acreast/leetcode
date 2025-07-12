# Last updated: 7/12/2025, 11:50:29 PM
from typing import List

class Solution:
    def minDays(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        
        def dfs(r, c, visited):
            if (r < 0 or r >= ROWS or c < 0 or c >= COLS or grid[r][c] == 0 or (r, c) in visited):
                return
            visited.add((r, c))
            neighbors = [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]
            for nr, nc in neighbors:
                dfs(nr, nc, visited)
        
        def count_islands():
            visited = set()
            island_count = 0
            for r in range(ROWS):
                for c in range(COLS):
                    if grid[r][c] == 1 and (r, c) not in visited:
                        dfs(r, c, visited)
                        island_count += 1
            return island_count
        
        # Initial island count
        if count_islands() != 1:
            return 0
        
        # Try removing one land cell and check the number of islands
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    grid[r][c] = 0
                    if count_islands() != 1:
                        return 1
                    grid[r][c] = 1
        
        # If still connected, return 2
        return 2
