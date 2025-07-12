# Last updated: 7/12/2025, 11:46:03 PM
class Solution:
    def robotWithString(self, s: str) -> str:
        count = Counter(s)
        stack = []
        res = []

        def min_char(freq):
            for i in range(26):
                ch = chr(ord('a') + i)
                if count[ch] > 0:
                    return ch
            return 'a'
        

        for char in s:
            stack.append(char)
            count[char] -= 1
            while stack and stack[-1] <= min_char(stack):
                res.append(stack.pop())
        
        while stack:
            res.append(stack.pop())
        
        return ''.join(res)