# Last updated: 7/12/2025, 11:50:45 PM
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        result = 0
        key = 0
        for idx, num in enumerate(nums):
            for idx, num in enumerate(nums):
                if num is nums[key] and key > idx:
                    result += 1
            key += 1
        
        return result