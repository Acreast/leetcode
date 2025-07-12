# Last updated: 7/12/2025, 11:45:12 PM
class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        def is_capable(capability):
            i = 0
            count = 0
            while i < len(nums):
                if nums[i] <= capability:
                    i += 2
                    count += 1
                else:
                    i += 1
                if count == k:
                    break
            return count == k

        l = min(nums)
        r = max(nums)
        res = 0

        while l <= r:
            mid = (l + r) // 2
            if is_capable(mid):
                res = mid
                r = mid - 1
            else:
                l = mid + 1
        
        return res