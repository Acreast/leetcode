# Last updated: 7/12/2025, 11:44:51 PM
class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        nums.sort()
        l, r = 0, 10 ** 9
        res = 10 ** 9
        if p == 0:
            return 0
        
        def is_valid(threshold):
            i, cnt = 0, 0
            while i < len(nums) - 1:
                if abs(nums[i] - nums[i + 1]) <= threshold:
                    cnt += 1
                    i += 2
                else:
                    i += 1
                if cnt == p:
                    return True
            return False

        while l <= r:
            m = l + (r - l) // 2
            if is_valid(m):
                res = m
                r = m - 1
            else:
                l = m + 1

        return res