# Last updated: 5/3/2025, 11:40:45 PM
class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        for target in [tops[0], bottoms[0]]:
            missing_t, missing_b = 0, 0
            for i, pair in enumerate(zip(tops,bottoms)):
                top, bottom = pair
                if not(top == target or bottom == target):
                    break
                if top != target:
                    missing_t += 1
                if bottom != target:
                    missing_b += 1
                if i == len(tops) - 1:
                    return min(missing_t, missing_b)
        return -1
            


