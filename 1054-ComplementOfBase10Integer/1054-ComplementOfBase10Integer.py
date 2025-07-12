# Last updated: 7/12/2025, 11:53:38 PM
class Solution(object):
    def bitwiseComplement(self, n):
        if(n==0):
            return 1
        result = 0
        factor = 1
        while(n>0):
            result += factor * (1 if n % 2 == 0 else 0)
            factor *= 2
            n /= 2
            
        return result