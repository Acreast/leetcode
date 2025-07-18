# Last updated: 7/12/2025, 11:44:50 PM
class Solution:
    def minimumTime(self, grid: List[List[int]]) -> int:
        if min(grid[0][1], grid[1][0]) > 1:
            return -1
        
        visit = set()
        min_heap = [(0, 0, 0)]
        ROWS, COLS = len(grid), len(grid[0])
        while min_heap:
            t, r, c = heapq.heappop(min_heap)
            if (r, c) == (ROWS - 1, COLS - 1):
                return t
            nei = [(r + 1, c), (r, c + 1), (r - 1 , c), (r, c - 1)]
            for nr, nc in nei:
                if nr < 0 or nc < 0 or (nr, nc) in visit or nr == ROWS or nc == COLS:
                    continue
                wait = 0
                if abs(grid[nr][nc] - t) % 2 == 0:
                    wait = 1
                n_time = max(grid[nr][nc] + wait, 1 + t)
                heapq.heappush(min_heap, (n_time, nr, nc))
                visit.add((nr, nc))



