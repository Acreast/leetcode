# Last updated: 7/12/2025, 11:45:11 PM
class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels = set("aeiou")

        prefix_cnt = [0] * (len(words) + 1)
        prev = 0
        for i, w in enumerate(words):
            if w[0] in vowels and w[-1] in vowels:
                prev += 1
            prefix_cnt[i + 1] = prev
        
        res = [0] * len(queries)

        for i, q in enumerate(queries):
            l, r = q
            res[i] = prefix_cnt[r + 1] - prefix_cnt[l]
        
        return res