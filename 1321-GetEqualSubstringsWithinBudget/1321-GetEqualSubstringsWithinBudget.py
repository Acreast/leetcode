# Last updated: 7/12/2025, 11:52:36 PM
class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        curCost = 0  # Current accumulated cost
        l = 0       # Left pointer of the window
        res = 0     # Result to store the maximum length of valid substring

        for r in range(len(s)):  # Right pointer of the window
            curCost += abs(ord(s[r]) - ord(t[r]))  # Add the cost of current character difference

            # If the current cost exceeds maxCost, move the left pointer to reduce the cost
            while curCost > maxCost:
                curCost -= abs(ord(s[l]) - ord(t[l]))
                l += 1

            # Update the result with the maximum length found
            res = max(res, r - l + 1)

        return res
