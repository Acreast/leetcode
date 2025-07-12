# Last updated: 7/12/2025, 11:48:00 PM
class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        for i in range(len(arr)):
            is_distinct = True
            for j in range(len(arr)):
                if i == j:
                    continue
                if arr[i] == arr[j]:
                    is_distinct = False
            if is_distinct:
                k -= 1
                if k == 0:
                    return arr[i]
        return ""
