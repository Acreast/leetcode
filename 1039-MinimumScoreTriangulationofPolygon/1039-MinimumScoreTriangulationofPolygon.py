# Last updated: 9/29/2025, 11:48:52 PM
class Solution:
    '''
    The recursive approach with memoization works as follows:
    Base case:
    If i+1=j
        There are only two vertices, so no triangle can be formed.
            Return 0.

    Memoization check:
        If we've already computed dp[i][j]
            Return the cached result.

    Try all possible middle vertices:
        For each k where i<k<j:
    '''
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

