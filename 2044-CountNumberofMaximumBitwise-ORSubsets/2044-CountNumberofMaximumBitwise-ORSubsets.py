# Last updated: 7/29/2025, 11:33:07 PM
class Solution:
    def smallestSubarrays(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n
        last = [-1] * 30

        for i in range(n -1, -1, -1):
            x = nums[i]
            j = i

            for b in range(30):
                if (x >> b) & 1:
                    last[b] = i
                if last[b] != -1:
                    j = max(last[b], j)
            res[i] = j - i + 1
        
        return res