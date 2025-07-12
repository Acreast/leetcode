# Last updated: 7/12/2025, 11:43:01 PM
class Solution:
    def compressedString(self, word: str) -> str:
        comp = ""
        counter = 1
        for i in range(1,len(word)):
            if word[i-1] == word[i]:
                counter += 1
                if counter > 9:
                    comp += str(counter - 1) + word[i]
                    counter = 1
            else:
                comp += str(counter) + word[i - 1]
                counter = 1

        comp += str(counter) + word[-1]
        return comp