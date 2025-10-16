# Last updated: 10/16/2025, 11:10:41 PM
class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        rem = [0] * value
        for x in nums:
            rem[x % value] += 1
        res = 0
        while rem[res % value]:
            rem[res % value] -= 1
            res += 1
        return res