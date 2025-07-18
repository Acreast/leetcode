# Last updated: 7/12/2025, 11:44:26 PM
class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        total_distinct = len(set(nums))
        n = len(nums)
        count = 0

        for i in range(n):
            seen = set()
            for j in range(i, n):
                seen.add(nums[j])
                if len(seen) == total_distinct:
                    count += n - j
                    break
        return count