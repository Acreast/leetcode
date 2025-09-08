# Last updated: 9/8/2025, 8:42:38 PM
class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        a = n - 1
        b = 1

        str_a = str(a)
        str_b = str(b)

        while ("0" in str_a or "0" in str_b) and a > 0 and b < n:
            a -= 1
            b += 1
            str_a = str(a)
            str_b = str(b)
        
        return [a, b]


            