# Last updated: 7/12/2025, 11:54:52 PM
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        
        def process_string(string):
            stack = []
            for char in string:
                if char != '#':
                    stack.append(char)
                elif stack:
                    stack.pop()
            return stack
        
        return process_string(s) == process_string(t)