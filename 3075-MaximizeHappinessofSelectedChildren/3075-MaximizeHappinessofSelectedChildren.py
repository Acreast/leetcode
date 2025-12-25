# Last updated: 12/25/2025, 7:51:24 PM
1class Solution:
2    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
3        happiness.sort(reverse=True)
4        res = sum(max(happiness[i] - i, 0) for i in range(k))
5        return res