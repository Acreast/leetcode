# Last updated: 7/17/2025, 11:46:27 PM
class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        N = len(nums)
        if k == 1:
            return N

        res = 2
        mod_arr = [0] * N

        for i in range(N):
            mod_arr[i] = nums[i] % k
        
        for i in range(k):
            dp = [0] * k
            for j in range(N):
                mod = mod_arr[j]
                pos = (i - mod + k) % k
                dp[mod] = dp[pos] + 1
                res = max(res, dp[mod])
        
        return res