# Last updated: 7/12/2025, 11:47:32 PM
class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        mpp = Counter(words)
        count = 0
        is_palindrome = 0
        for w, freq in mpp.items():
            s = w[::-1]
            if w == s:
                count += (freq//2) * 4
                if freq % 2:
                    is_palindrome = 1
            elif w < s and s in mpp:
                count += min(freq, mpp[s]) * 4
        return count + is_palindrome * 2