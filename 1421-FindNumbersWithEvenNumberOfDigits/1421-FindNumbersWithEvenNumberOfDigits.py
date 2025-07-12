# Last updated: 7/12/2025, 11:52:08 PM
class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        res =  0
        for num in nums:
            num_str = str(num)
            if len(num_str) % 2 == 0:
                res += 1
        return res