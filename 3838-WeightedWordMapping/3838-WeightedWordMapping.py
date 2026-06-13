# Last updated: 6/14/2026, 12:46:51 AM
1class Solution:
2    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
3        
4        res = ""
5        for word in words:
6            word_weight = 0
7            for c in word:
8                pos = ord(c) - ord('a')
9                word_weight += weights[pos] 
10            res += (chr(ord('z') - (word_weight % 26)))
11
12        return res