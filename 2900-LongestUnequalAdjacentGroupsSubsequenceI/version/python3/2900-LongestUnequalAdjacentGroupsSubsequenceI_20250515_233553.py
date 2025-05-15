# Last updated: 5/15/2025, 11:35:53 PM
class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        res = []
        last = -1
        for i in range(len(words)):
            if groups[i] != last:
                res.append(words[i])
                last = groups[i]

        return res