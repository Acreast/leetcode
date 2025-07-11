# Last updated: 7/12/2025, 11:53:05 PM
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        arr2_set = set(arr2)
        end = []
        arr1_count = defaultdict(int)
        for n in arr1:
            if n not in arr2_set:
                end.append(n)
            arr1_count[n] += 1
        end.sort()

        res = []
        for n in arr2:
            for _ in range(arr1_count[n]):
                res.append(n)
        
        return res + end