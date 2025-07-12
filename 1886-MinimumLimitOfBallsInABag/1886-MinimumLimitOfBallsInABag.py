# Last updated: 7/12/2025, 11:49:17 PM
class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        def is_dividable(max_balls):
            num_ops = 0
            for n in nums:
                num_ops += ceil(n/max_balls) - 1
                if num_ops > maxOperations:
                    return False
            return True

        l, r = 1, max(nums)
        while l < r:
            m = l + ((r - l) // 2)
            if is_dividable(m):
                r = m
            else:
                l = m + 1
        return l