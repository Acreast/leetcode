# Last updated: 12/7/2025, 7:29:32 PM
1class Solution:
2    def countOdds(self, low: int, high: int) -> int:
3        if low % 2 or high % 2:
4            return (high - low) // 2  + 1
5        else:
6            return (high - low) // 2