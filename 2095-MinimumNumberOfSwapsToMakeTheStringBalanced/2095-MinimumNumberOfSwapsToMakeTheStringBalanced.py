# Last updated: 7/12/2025, 11:48:21 PM
class Solution:
    def minSwaps(self, s: str) -> int:
        close, maxClosed = 0, 0

        for c in s:
            if c == "[":
                close -= 1
            else:
                close += 1
            maxClosed = max(close, maxClosed)
        
        return (maxClosed + 1) // 2