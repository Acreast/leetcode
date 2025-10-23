# Last updated: 10/23/2025, 8:52:48 PM
class Solution:
    def hasSameDigits(self, s: str) -> bool:
        
        while len(s) > 2:
            new_str = ""
            for i in range(1, len(s)):
                new_digit = (int(s[i - 1]) + int(s[i])) % 10
                new_str = new_str + str(new_digit)
            s = new_str

        return s[0] == s[1]