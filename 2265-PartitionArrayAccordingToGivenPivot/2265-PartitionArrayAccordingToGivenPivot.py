# Last updated: 7/12/2025, 11:47:19 PM
class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        less = []
        equal = []
        more = []

        for num in nums:
            if num < pivot:
                less.append(num)
            elif num > pivot:
                more.append(num)
            else:
                equal.append(num)
        
        return less + equal + more