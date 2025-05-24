# Last updated: 5/24/2025, 12:50:13 PM
class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        res = []
        for i,word in enumerate(words):
            for c in word:
                if c == x:
                    res.append(i)
                    break
        
        return res