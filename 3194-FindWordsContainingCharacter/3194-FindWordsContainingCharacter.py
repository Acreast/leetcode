# Last updated: 7/12/2025, 11:43:50 PM
class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        res = []
        for i,word in enumerate(words):
            for c in word:
                if c == x:
                    res.append(i)
                    break
        
        return res