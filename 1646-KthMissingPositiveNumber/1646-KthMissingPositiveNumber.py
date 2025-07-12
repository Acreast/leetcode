# Last updated: 7/12/2025, 11:50:41 PM
class Solution(object):
    def findKthPositive(self, arr, k):
        l, r = 0, len(arr)
        while l < r:
            m = (l + r) / 2
            if arr[m] - 1 - m < k:
                l = m + 1
            else:
                r = m
        return l + k