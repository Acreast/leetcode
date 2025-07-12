# Last updated: 7/12/2025, 11:54:36 PM
class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        res = 0
        arr_set = set(arr)


        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):

                prev, cur = arr[i], arr[j]
                next = cur + prev
                length = 2
                while next in arr_set:
                    length += 1
                    prev = cur
                    cur = next
                    next = prev + cur
                    res = max(res, length)
        return res
                    
