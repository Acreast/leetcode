# Last updated: 7/12/2025, 11:50:54 PM
class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        MOD = 10 ** 9 + 7
        sub_sum = []
        for i in range(n):
            cur_sum = 0
            for j in range(i,n):
                cur_sum = (cur_sum + nums[j]) % MOD
                sub_sum.append(cur_sum)
        
        sub_sum.sort()
        res = 0
        for n in range(left-1, right):
            res = (res + sub_sum[n]) % MOD
        return res
