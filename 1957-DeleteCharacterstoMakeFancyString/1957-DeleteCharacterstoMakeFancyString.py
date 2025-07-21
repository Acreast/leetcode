# Last updated: 7/22/2025, 12:24:00 AM
class Solution:
    def makeFancyString(self, s: str) -> str:
        res = ''
        for i in range(len(s)):
            if len(res) >= 1:
                if s[i] == res[-1]:
                    if len(res) >= 2:
                        if s[i] == res[-2]:
                            continue
            res += s[i]

        return res
