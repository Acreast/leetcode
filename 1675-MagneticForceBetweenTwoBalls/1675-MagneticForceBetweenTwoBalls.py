# Last updated: 7/12/2025, 11:50:33 PM
class Solution(object):
    def maxDistance(self, position, m):
        position.sort()
        lo, hi = 1, (position[-1] - position[0]) // (m - 1)
        ans = 1
        
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if self.canWePlace(position, mid, m):
                ans = mid
                lo = mid + 1
            else:
                hi = mid - 1
        
        return ans
    
    def canWePlace(self, arr, dist, balls):
        countBalls = 1
        lastPlaced = arr[0]
        for i in range(1, len(arr)):
            if arr[i] - lastPlaced >= dist:
                countBalls += 1
                lastPlaced = arr[i]
            if countBalls >= balls:
                return True
        return False