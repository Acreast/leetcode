# Last updated: 12/20/2025, 1:38:26 PM
1class Solution:
2    def minDeletionSize(self, strs: List[str]) -> int:
3        res = 0
4        for c in range(len(strs[0])):
5            for s in range(1, len(strs)):
6                if ord(strs[s][c]) < ord(strs[s - 1][c]):
7                    res += 1
8                    break
9        return res
10        
11            
12