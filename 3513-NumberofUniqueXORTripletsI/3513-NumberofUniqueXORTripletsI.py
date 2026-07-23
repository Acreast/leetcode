# Last updated: 7/24/2026, 1:12:12 AM
1class Solution:
2    def uniqueXorTriplets(self, nums: List[int]) -> int:
3        n = len(nums)        
4        return 1 << (n.bit_length() - 3 // (n + 1))