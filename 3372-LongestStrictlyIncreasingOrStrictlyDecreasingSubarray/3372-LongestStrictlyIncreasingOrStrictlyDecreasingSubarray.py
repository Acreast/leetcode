# Last updated: 7/12/2025, 11:43:16 PM
class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        max_count = 1
        count = 1
        prev_flag = None
        for i in range(1, len(nums)):
            cur_flag = None
            if nums[i] < nums[i - 1]:
                cur_flag = False
            elif nums[i] > nums[i - 1]:
                cur_flag = True

            if nums[i] == nums[i - 1] or cur_flag == None:
                count = 1
                prev_flag = None  # Reset prev_flag for consecutive duplicates
                continue
                
            if cur_flag == prev_flag or prev_flag == None:
                count += 1
            else:
                count = 2  # Reset to 2 when switching direction

            prev_flag = cur_flag
            max_count = max(max_count, count)
        
        return max_count
