# Last updated: 7/17/2025, 12:10:33 AM
class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        even_count = 0
        odd_count = 0
        for num in nums:
            if num % 2 == 0:
                even_count += 1
            else:
                odd_count += 1
        
        even_end = 0
        odd_end = 0
        for num in nums:
            if num % 2 == 0:
                even_end = max(even_end, odd_end + 1)
            else:
                odd_end = max(odd_end, even_end + 1)
        return max(even_count, odd_count, even_end, odd_end)