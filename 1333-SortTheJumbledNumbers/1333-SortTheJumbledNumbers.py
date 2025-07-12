# Last updated: 7/12/2025, 11:52:29 PM
class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        pairs = []
        
        for i, n in enumerate(nums):
            n = str(n)
            val = 0
            for num in n:
                val *= 10
                val += mapping[int(num)]
            
            pairs.append((val, i))
        pairs.sort()
        return [nums[p[1]] for p in pairs]