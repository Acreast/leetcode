# Last updated: 6/17/2025, 10:59:16 PM
class Solution:
    
    def countGoodArrays(self, n: int, m: int, k: int) -> int:
        #????????
        return m*pow(m-1, n-k-1, mod:=10**9+7)*comb(n-1, k)%mod

        
