# Last updated: 7/12/2025, 11:52:56 PM
class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        count = defaultdict(int)

        for a, b in dominoes:
            key = tuple(sorted((a, b)))
            count[key] += 1

        res = 0
        for val in count.values():
            res += val * (val - 1) // 2
        return res



