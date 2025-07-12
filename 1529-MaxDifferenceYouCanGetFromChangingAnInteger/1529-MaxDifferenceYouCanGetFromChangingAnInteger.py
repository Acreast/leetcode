# Last updated: 7/12/2025, 11:51:27 PM
class Solution:
    def maxDiff(self, num: int) -> int:
        s = str(num)
        to_replace_char = ''
        for c in s:
            if c!= '9':
                to_replace_char = c
                break
        max_str = ''.join(['9' if c == to_replace_char else c for c in s])

        if s[0] != '1':
            to_replace_char = s[0]
            min_str = ''.join(['1' if ch == to_replace_char else ch for ch in s])
        else:
            to_replace_char = ''
            for ch in s[1:]:  
                if ch != '0' and ch != '1':
                    to_replace_char = ch
                    break
            if to_replace_char:
                min_str = ''.join(['0' if ch == to_replace_char else ch for ch in s])
            else:
                min_str = s

        return int(max_str) - int(min_str)