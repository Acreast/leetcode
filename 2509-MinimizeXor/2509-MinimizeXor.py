# Last updated: 7/12/2025, 11:46:06 PM
class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        
        def bit_counter(n):
            res = 0
            while n > 0:                
                res += 1 & n
                n = n >> 1
            return res
        
        cnt1, cnt2 = bit_counter(num1), bit_counter(num2)
        x = num1
        i = 0

        while cnt1 > cnt2:
            if x & (1 << i):
                cnt1 -= 1
                x = x ^ (1 << i)
            i += 1
        
        while cnt1 < cnt2:
            if x & (1 << i) == 0:
                cnt1 += 1
                x = x | (1 << i)
            i += 1
        
        return x