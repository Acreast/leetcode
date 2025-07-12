# Last updated: 7/12/2025, 11:43:02 PM
class Solution:
    def clearDigits(self, s: str) -> str:
        stack = []
        for c in s:
            if c.isdigit():
                stack.pop()
            else:
                stack.append(c)
        
        return "".join(stack)