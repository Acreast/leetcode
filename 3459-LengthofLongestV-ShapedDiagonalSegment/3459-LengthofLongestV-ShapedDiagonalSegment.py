# Last updated: 8/27/2025, 11:36:47 PM
class Solution:
    def lenOfVDiagonal(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dirs = ((-1, 1), (1, 1), (1, -1), (-1, -1))

        @lru_cache(None)
        def dfs(i, j, turned, num, d_idx):
            if not (0 <= i < m and 0 <= j < n): return 0
            if grid[i][j] != num: return 0

            next_num = 0 if num == 2 else 2
            di, dj = dirs[d_idx]

            res = 1 + dfs(i + di, j + dj, turned, next_num, d_idx)

            if not turned:
                # Turn clockwise 90°
                new_di, new_dj = dj, -di
                new_dir = dirs.index((new_di, new_dj))
                res = max(res, 1 + dfs(i + new_di, j + new_dj, True, next_num, new_dir))

            return res

        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    for d_idx, (di, dj) in enumerate(dirs):
                        ans = max(ans, 1 + dfs(i + di, j + dj, False, 2, d_idx))
        return ans