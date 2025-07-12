# Last updated: 7/12/2025, 11:43:48 PM
class Solution:
    def minimumSteps(self, s: str) -> int:
        r = 0 
        l = 0
        res = 0

        while (r < len(s)):
            if s[r] == "0":
                res += (r - l)
                l += 1
            r += 1
        
        return res