# Last updated: 7/27/2025, 9:57:37 PM
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        stack.append(s[0])
        for i in range(1, len(s)):
            stack.append(s[i])
            while stack and len(stack) > 1:
                if stack[-2] == '(' and stack[-1] == ")":
                    stack.pop()
                    stack.pop()
                elif stack[-2] == '{' and stack[-1] == "}":
                    stack.pop()
                    stack.pop()
                elif stack[-2] == '[' and stack[-1] == "]":
                    stack.pop()
                    stack.pop()
                else:
                    break
            
                

        if len(stack) == 0:
            return True
        else:
            return False


