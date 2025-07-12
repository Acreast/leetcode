# Last updated: 7/12/2025, 11:43:58 PM
class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        sum1, sum2 = 0, 0
        num_zero1, num_zero2 = 0, 0
        for num in nums1:
            if num == 0:
                num_zero1 += 1
            sum1 += num
        for num in nums2:
            if num == 0:
                num_zero2 += 1
            sum2 += num
        

        if num_zero1 == 0 and num_zero2 == 0:
            return sum1 if sum1 == sum2 else -1
        
        elif num_zero1 == 0:
            return sum1 if sum2 + num_zero2 <= sum1 else -1
        
        elif num_zero2 == 0:
            return sum2 if sum1 + num_zero1 <= sum2 else -1
        
        return max(sum1 + num_zero1, sum2 + num_zero2)