# Last updated: 9/15/2025, 10:48:07 PM
class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        
        word_arr = text.split(" ")
        res = 0
        for word in word_arr:
            has_broken = False
            for c in brokenLetters:
                if c in word:
                    has_broken = True
                    break
            
            if not has_broken:
                res += 1
            
        return res
            
