# Last updated: 7/12/2025, 11:44:19 PM
class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        left = defaultdict(int)
        right = Counter(nums)

        for i in range(len(nums)):
            left[nums[i]] += 1
            right[nums[i]] -= 1

            left_len = i + 1
            right_len = len(nums) - i - 1

            if 2 * left[nums[i]] > left_len and 2 * right[nums[i]] > right_len:
                return i
        
        return -1
