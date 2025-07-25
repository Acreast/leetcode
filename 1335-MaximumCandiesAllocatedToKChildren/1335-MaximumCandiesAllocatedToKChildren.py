# Last updated: 7/12/2025, 11:52:28 PM
class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        total = sum(candies)

        if total < k:
            return 0

        l = 1
        r = total//k
        res = 0

        while l <= r:
            m = ( l + r ) // 2
            count = 0
            for c in candies:
                if c >= m:
                    count += c // m
                if count >= k:
                    break
            
            if count >= k:
                res = m
                l = m + 1
            else:
                r = m - 1
        return res