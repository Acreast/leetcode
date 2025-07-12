# Last updated: 7/12/2025, 11:51:10 PM
class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        
        sentence = sentence.split()

        for i, word in enumerate(sentence):
            if word.startswith(searchWord):
                return i + 1
        return -1