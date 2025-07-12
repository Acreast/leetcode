# Last updated: 7/12/2025, 11:53:30 PM
class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        cache = {}

        def dfs(i):
            if i in cache:
                return cache[i]
            
            result = 0
            curr_max = 0
            for j in range(i, min(len(arr), k + i)):
                curr_max = max(arr[j], curr_max)
                window_size = (j - i + 1)
                result = max(result, dfs(j+1) + curr_max * window_size)
            cache[i] = result
            return result
        
        return dfs(0)
