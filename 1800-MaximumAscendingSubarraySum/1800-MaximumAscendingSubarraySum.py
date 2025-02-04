class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        cur_count = nums[0]
        max_count = cur_count

        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                cur_count += nums[i]
            else:
                cur_count = nums[i]

            max_count = max(cur_count, max_count)

        return max_count