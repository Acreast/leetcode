# Last updated: 9/29/2025, 11:46:55 PM
class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        dp = [[0] * 50 for _ in range(50)]
        
        def top_down(i, j, res):
            if j == 0:
                j = len(values) - 1
            if dp[i][j] != 0:
                return dp[i][j]
            for k in range(i + 1, j):
                res = min(
                    res if res != 0 else float('inf'),
                    top_down(i, k, 0) +  
                    values[i] * values[k] * values[j] +
                    top_down(k, j, 0)    
                )
            dp[i][j] = res
            return dp[i][j]
        
        return top_down(0, 0, 0)

