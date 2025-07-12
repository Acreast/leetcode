# Last updated: 7/12/2025, 11:54:11 PM
class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        res = 0
        open = 0

        for c in s:
            if c == "(":
                open += 1
            else:
                if open == 0:
                    res += 1
                else:
                    open = max(open - 1, 0)
        return open + res
            