# Last updated: 7/12/2025, 11:51:34 PM
class Solution:
    def numTeams(self, rating: List[int]) -> int:
        res = 0
        for m in range(1, len(rating) -1):
            left_smaller = right_larger = 0
            for i in range(m):
                if rating[i] < rating[m]:
                    left_smaller += 1
            for i in range(m+1, len(rating)):
                if rating[i] > rating[m]:
                    right_larger += 1
            
            res += left_smaller * right_larger

            left_larger = m - left_smaller
            right_smaller = len(rating) - m - 1 - right_larger
            res += left_larger * right_smaller
        return res