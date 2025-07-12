# Last updated: 7/12/2025, 11:51:15 PM
class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        return Counter(target) == Counter(arr)