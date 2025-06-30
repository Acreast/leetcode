# Last updated: 7/1/2025, 12:06:07 AM
class Solution:
    def findLHS(self, nums: List[int]) -> int:
        count_map = Counter(nums)
        res = 0
        for num, count in count_map.items():
            if num + 1 in count_map.keys():
                res = max(res, count_map[num] + count_map[num + 1])
            
        return res
