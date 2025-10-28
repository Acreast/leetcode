# Last updated: 10/29/2025, 12:05:09 AM
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        res = r 

        while l <= r:
            time = 0
            mid = (l + r) // 2

            for p in piles:
                time += math.ceil(p / mid)
            
            if time <= h:
                res = min(res, mid)
                r = mid - 1
            else:
                l = mid + 1


        return res


