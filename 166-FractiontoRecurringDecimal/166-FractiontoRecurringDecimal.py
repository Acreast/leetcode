# Last updated: 9/25/2025, 12:00:26 AM
class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return "0"
        
        res = []

        if (numerator < 0) ^ (denominator < 0):
            res.append("-")
        
        num, den = abs(numerator), abs(denominator)
        res.append(str(num // den))
        remainder = num % den
        if remainder == 0:
            return "".join(res)

        res.append(".")
        seen = {}
        while remainder:
            if remainder in seen:
                index = seen[remainder]
                res.insert(index, "(")
                res.append(")")
                return "".join(res)
            seen[remainder] = len(res)
            remainder *= 10
            res.append(str(remainder // den))
            remainder %= den

        return "".join(res)
