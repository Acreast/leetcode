# Last updated: 7/12/2025, 11:45:41 PM
class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        words = sentence.split()
        
        # Check the last letter of each word with the first letter of the next word
        for i in range(len(words) - 1):
            if words[i][-1] != words[i + 1][0]:
                return False
        
        # Check if the sentence is circular by comparing the last letter of the last word with the first letter of the first word
        return words[-1][-1] == words[0][0]
