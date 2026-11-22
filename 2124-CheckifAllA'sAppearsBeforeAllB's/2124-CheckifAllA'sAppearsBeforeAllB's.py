# Last updated: 11/22/2026, 6:31:15 PM
1class Solution:
2    def checkString(self, s: str) -> bool:
3        b_found = False
4        for c in s:
5            if c == 'b':
6                b_found = True
7            else:
8                if b_found:
9                    return False
10        return True
11