# Last updated: 7/12/2025, 11:45:53 PM
class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        cur_sum = 0
        count = defaultdict(int)
        l = 0

        for r in range(len(nums)):
            cur_sum += nums[r]
            count[nums[r]] += 1

            if r - l + 1 > k:
                count[nums[l]] -= 1
                if count[nums[l]] == 0:
                    count.pop(nums[l])
                cur_sum -= nums[l]
                l += 1

            if r - l + 1 == k and len(count) == k:
                res = max(res, cur_sum)
            

        return res