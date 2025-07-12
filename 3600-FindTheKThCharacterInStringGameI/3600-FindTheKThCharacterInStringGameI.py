# Last updated: 7/12/2025, 11:42:47 PM
class Solution:
    def kthCharacter(self, k: int) -> str:
        return chr(ord('a') + (k - 1).bit_count())