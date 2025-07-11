# Last updated: 7/12/2025, 11:42:57 PM
class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        N = len(colors)
        res = 0
        l = 0
        for r in range(1, N + k - 1):
            if colors[r % N] == colors[(r - 1) % N]:
                l = r
            
            if r - l + 1 > k:
                l += 1
            if r - l + 1 == k:
                res += 1
        
        return res