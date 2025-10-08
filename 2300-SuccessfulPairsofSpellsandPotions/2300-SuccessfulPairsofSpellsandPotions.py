# Last updated: 10/9/2025, 12:20:35 AM
class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        res = []

        for s in spells:
            index = len(potions)
            l = 0
            r = len(potions) - 1
            while l <= r:
                m = (r + l) // 2
                if potions[m] * s >= success:
                    r = m - 1
                    index = m
                else:
                    l = m + 1

            res.append(len(potions) - index)


        return res