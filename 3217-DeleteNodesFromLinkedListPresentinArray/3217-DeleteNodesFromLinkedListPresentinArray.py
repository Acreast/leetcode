# Last updated: 11/2/2025, 7:02:14 PM
class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        
        grid = [[0] * n for _ in range(m)]
        # 0 = unguarded
        # 1 = guarded
        # 2 = the guard
        # 3 = wall

        for r, c in guards:
            grid[r][c] = 2
        
        for r, c in walls:
            grid[r][c] = 3
        
        def mark_guarded(guard_row, guard_col):
            for r in range(guard_row + 1, m):
                if grid[r][guard_col] in [2, 3]:
                    break
                grid[r][guard_col] = 1
            for r in reversed(range(0, guard_row)):
                if grid[r][guard_col] in [2, 3]:
                    break
                grid[r][guard_col] = 1
            for c in range(guard_col + 1, n):
                if grid[guard_row][c] in [2, 3]:
                    break
                grid[guard_row][c] = 1
            for c in reversed(range(0, guard_col)):
                if grid[guard_row][c] in [2, 3]:
                    break
                grid[guard_row][c] = 1
        
        for r, c in guards:
            mark_guarded(r, c)
        res = 0
        for row in grid:
            for cell in row:
                if cell == 0:
                    res += 1

        return res