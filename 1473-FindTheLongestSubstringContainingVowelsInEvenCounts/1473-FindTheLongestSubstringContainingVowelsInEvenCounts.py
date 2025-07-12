# Last updated: 7/12/2025, 11:51:48 PM
class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        vowels = 'aeiou'

        res = 0
        mask = 0
        mask_to_index = {0:-1}

        for i, c in enumerate(s):
            if c in vowels:
                mask = mask ^ (1 + ord(c) - ord('a'))
            if mask in mask_to_index:
                length = i - mask_to_index[mask]
                res = max(res, length)
            else:
                mask_to_index[mask] = i
        return res