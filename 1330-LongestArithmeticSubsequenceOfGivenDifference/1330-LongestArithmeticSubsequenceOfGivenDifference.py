# Last updated: 7/12/2025, 11:52:33 PM
class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:

        dp = {}
        max_length = 1
        
        for num in arr:
            if num - difference in dp:
                dp[num] = dp[num - difference] + 1 

            else:
                dp[num] = 1

            max_length = max(max_length, dp[num])

        return max_length
