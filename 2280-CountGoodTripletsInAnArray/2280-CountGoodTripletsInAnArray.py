# Last updated: 7/12/2025, 11:47:15 PM
class Solution:
    def goodTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        index = {}
        for i, v in enumerate(nums1):
            index[v] = i
        n = len(nums2)
        total = 0
        stack = []
        for num in nums2:
            i = index[num]
            left = bisect.bisect_left(stack, i)
            right = (n - 1 - i) - (len(stack) - left)
            total += left * right
            bisect.insort(stack,i)
        return total