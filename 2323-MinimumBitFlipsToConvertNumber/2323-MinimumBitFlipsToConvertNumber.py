# Last updated: 7/12/2025, 11:47:06 PM
class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        res = 0
        while (start or goal):
            if (start & 1) != (goal & 1):
                res += 1
            start = start // 2
            goal = goal // 2
        
        return res