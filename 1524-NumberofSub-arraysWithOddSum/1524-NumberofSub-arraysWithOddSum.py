class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        odd_cnt = 0
        even_cnt = 0
        res = 0
        mod = 10**9 + 7
        cur_sum = 0

        for num in arr:
            cur_sum += num

            if cur_sum % 2:
                odd_cnt += 1
                res = (res + 1 + even_cnt) % mod
            else:
                even_cnt += 1
                res = (res + odd_cnt) %  mod
        
        return res

