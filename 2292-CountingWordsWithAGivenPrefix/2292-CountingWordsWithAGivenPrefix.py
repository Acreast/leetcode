# Last updated: 7/12/2025, 11:47:14 PM
class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:

        res = 0
        for word in words:
            if re.match(f"^{pref}",word):
                res += 1

        return res