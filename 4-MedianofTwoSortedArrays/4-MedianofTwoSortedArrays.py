# Last updated: 11/22/2025, 5:49:55 PM
class Solution:
    def findMedianSortedArrays(self, A: List[int], B: List[int]) -> float:
        
        if len(A) > len(B):
            A, B = B, A
        max_size = len(A) + len(B)

        half = max_size // 2
        l = 0
        r = len(A) - 1

        while True:
            a_mid = (l + r) // 2
            b_mid = half - a_mid - 2

            a_left = A[a_mid] if a_mid >= 0 else float("-infinity")
            a_right = A[a_mid + 1] if (a_mid + 1) < len(A) else float("infinity")
            b_left = B[b_mid] if b_mid >= 0 else float("-infinity")
            b_right = B[b_mid + 1] if (b_mid + 1) < len(B) else float("infinity")
        
            if a_left <= b_right and b_left <= a_right:
                if max_size % 2:
                    return min(a_right, b_right)
                return (max(a_left, b_left) + min(a_right, b_right)) /2
            elif a_left > b_right:
                r = a_mid - 1
            else:
                l = a_mid + 1
        
            

            


