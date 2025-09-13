# Last updated: 9/13/2025, 10:33:25 AM
class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = [c for c in s if c in "aeiouAEIOU"]

        # Sort vowels in reverse order
        vowels.sort(reverse=True)

        res = []
        for c in s:
            if c in "aeiouAEIOU":
                res.append(vowels.pop())  # Take from the end (smallest remaining)
            else:
                res.append(c)

        return "".join(res)
