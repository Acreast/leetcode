# Last updated: 7/3/2025, 11:40:42 PM
class Solution:
    def kthCharacter(self, k: int) -> str:
        return chr(ord('a') + (k - 1).bit_count())