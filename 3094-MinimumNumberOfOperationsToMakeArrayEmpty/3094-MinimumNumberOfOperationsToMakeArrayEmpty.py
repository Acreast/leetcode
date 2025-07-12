# Last updated: 7/12/2025, 11:44:05 PM
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        count = Counter(nums)
        res = 0
        for n,c in count.items():
            if c == 1:
                return -1
            res += ceil(c/3)

        return res
