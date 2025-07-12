# Last updated: 7/12/2025, 11:53:40 PM
class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        cnt = Counter(words[0])

        for w in words[1:]:  # Start from the second word
            cur_cnt = Counter(w)
            for c in cnt:
                cnt[c] = min(cnt[c], cur_cnt[c])  # Update the counts

        res = []
        for c in cnt:
            res.extend([c] * cnt[c])  # Append the character `cnt[c]` times to the result
        return res