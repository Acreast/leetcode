# Last updated: 7/12/2025, 11:52:44 PM
class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        cons_odd = 0
        for num in arr:
            if num % 2 != 0:
                cons_odd += 1
            else:
                cons_odd = 0
            if cons_odd == 3:
                return True
        return False