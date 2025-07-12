# Last updated: 7/12/2025, 11:42:45 PM
class Solution:
    def possibleStringCount(self, word: str) -> int:
        cur_count = 1
        res = 1
        for i in range(len(word) - 1):
            if word[i] == word[i + 1]:
                cur_count += 1
            else:
                if cur_count > 1:
                    res += cur_count - 1
                cur_count = 1
            if i == len(word) - 2 and cur_count > 1:
                res += cur_count - 1
        return res

