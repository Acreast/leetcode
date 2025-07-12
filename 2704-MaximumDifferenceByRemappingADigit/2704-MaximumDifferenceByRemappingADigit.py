# Last updated: 7/12/2025, 11:45:02 PM
class Solution:
    def minMaxDifference(self, num: int) -> int:
        s = str(num)
        to_replace_char = ''
        for c in s:
            if c!= '9':
                to_replace_char = c
                break
        max_str = ''.join(['9' if c == to_replace_char else c for c in s])

        to_replace_char = s[0]
        min_str = ''.join(['0' if c == to_replace_char else c for c in s])

        return int(max_str) - int(min_str)
                