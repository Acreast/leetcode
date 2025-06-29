# Last updated: 6/29/2025, 10:43:25 PM
class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        nums_map = [(num, i) for i, num in enumerate(nums)]

        nums_map.sort(key = lambda x: -x[0])

        top_kth = sorted(nums_map[:k], key = lambda x: x[1])

        return [num for num, _ in top_kth]
        
                