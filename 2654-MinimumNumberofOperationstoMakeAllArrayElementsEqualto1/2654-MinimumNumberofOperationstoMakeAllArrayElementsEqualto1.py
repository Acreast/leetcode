# Last updated: 11/13/2025, 12:45:39 AM
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        one_count = 0
        for n in nums:
            if n == 1:
                one_count += 1
        if one_count > 0:
            return len(nums) - one_count

        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        min_sub_len = float("inf")
        for l in range(len(nums)):
            cur_gcd = 0
            for r in range(l, len(nums)):
                if r - l + 1 >= min_sub_len:
                    break
                cur_gcd = gcd(cur_gcd, nums[r])
                if cur_gcd == 1:
                    min_sub_len = r - l + 1
                    break

        if min_sub_len == float("inf"):
            return -1
        return (len(nums) - 1) + (min_sub_len - 1)