# Last updated: 10/6/2025, 11:43:25 PM
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        N = len(grid)
        minHeap = [[grid[0][0], 0, 0]]
        visit = set()
        neighbors = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        while minHeap:
            t, r, c = heapq.heappop(minHeap)

            if r == N - 1 and c == N - 1:
                return t
            
            for neiR, neiC in neighbors:
                dr = r + neiR
                dc = c + neiC
                if (
                    dr < 0 or dc < 0 or dr == N or dc == N or
                    (dr, dc) in visit
                ):
                    continue
                visit.add((dr,dc))
                heapq.heappush(minHeap, [max(t, grid[dr][dc]), dr, dc])