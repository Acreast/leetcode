# Last updated: 7/29/2026, 12:13:46 AM
1class Solution:
2    def smallestPalindrome(self, s: str) -> str:
3        n = len(s)
4        freq = Counter(s[:n >> 1])
5
6        half = "".join(c * freq[c] for c in ascii_lowercase)
7        mid = s[n >> 1] if n & 1 else ""
8
9        return half + mid + half[::-1]