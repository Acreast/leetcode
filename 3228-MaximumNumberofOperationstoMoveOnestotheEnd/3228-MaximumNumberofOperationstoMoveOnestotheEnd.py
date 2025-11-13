# Last updated: 11/14/2025, 12:21:30 AM
class Solution:
    def maxOperations(self, s: str) -> int:
        ones = 0
        res = 0
        for i in range(len(s)):
            if s[i] == '1':
                ones += 1
            elif i > 0 and s[i - 1] == "1":
                res += ones
        return res