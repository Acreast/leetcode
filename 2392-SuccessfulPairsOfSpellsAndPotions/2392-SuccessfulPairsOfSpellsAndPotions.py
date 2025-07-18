# Last updated: 7/12/2025, 11:46:50 PM
class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        pairs = []
        for s in spells:
            factor = (success + s - 1) // s
            pairs.append(len(potions) - bisect.bisect_left(potions, factor))
        return pairs