# Last updated: 7/12/2025, 11:46:30 PM
class Solution:
    def smallestNumber(self, pattern: str) -> str:
        res = []
        stack = []

        for i in range(len(pattern) + 1):
            stack.append(i + 1)

            while stack and (i == len(pattern) or pattern[i] == "I"):
                res.append(str(stack.pop()))
        
        return "".join(res)
