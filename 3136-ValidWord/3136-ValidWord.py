# Last updated: 7/15/2025, 11:25:39 PM
class Solution:
    import re
    def isValid(self, word: str) -> bool:
        if len(word) < 3:
            return False
        # if not re.search(r"\d", word) and not re.search(r"[a-z]", word, re.IGNORECASE):
        #     return False
        if not re.search(r"[aeiou]",word,re.IGNORECASE):
            return False
        if not re.search(r"[bcdfghjklmnpqrstvwxyz]", word, re.IGNORECASE):
            return False
        for c in word:
            if not c.isalpha() and not c.isnumeric():
                return False
        
        return True