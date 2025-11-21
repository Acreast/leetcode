# Last updated: 11/21/2025, 11:11:00 PM
class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        char_dict = Counter(s)
        left_dict = set()
        res = set()
        for c in s:
            char_dict[c] -= 1
            for left_c in left_dict:
                if char_dict[left_c] > 0:
                    res.add((c,left_c))
            left_dict.add(c)
        
        return len(res)



        
