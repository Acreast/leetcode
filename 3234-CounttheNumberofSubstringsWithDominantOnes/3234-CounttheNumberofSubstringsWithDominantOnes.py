# Last updated: 11/16/2025, 12:43:09 AM
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)
        next_zeroes = [n] * (n)

        for i in range(n - 2, -1, -1):
            if s[i + 1] == "0":
                next_zeroes[i] = i + 1
            else:
                next_zeroes[i] = next_zeroes[i + 1]
        
        res = 0
        for l in range(n):
            zeroes = 1 if s[l] == "0" else 0
            r = l

            while zeroes * zeroes <= n:
                next_z = next_zeroes[r] if r < n else n
                ones = (next_z - l) - zeroes
                if ones >= zeroes * zeroes:
                    res += min(
                        next_z - r,
                        ones - zeroes*zeroes + 1
                    )
                r = next_z
                zeroes += 1
                if r == n:
                    break

        return res

