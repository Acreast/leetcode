# Last updated: 10/13/2025, 8:26:58 PM
class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        n = len(words)
        freq = [Counter(w) for w in words]
        res = [words[0]]
        for i in range(1, n):
            if freq[i] != freq[i - 1]:
                res.append(words[i])
        return res
