# Last updated: 7/12/2025, 11:55:22 PM
class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        cur_max = -1
        res = 0
        for i, n in enumerate(arr):
            cur_max = max(n, cur_max)
            if cur_max == i:
                res += 1

        return res
