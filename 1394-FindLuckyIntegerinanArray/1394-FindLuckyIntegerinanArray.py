# Last updated: 7/5/2025, 11:49:01 PM
class Solution:
    def findLucky(self, arr: List[int]) -> int:
        counter = Counter(arr)
        max_val = -1
        for num, count in counter.items():
            if num == count:
                max_val = max(num, max_val)
        
        return max_val