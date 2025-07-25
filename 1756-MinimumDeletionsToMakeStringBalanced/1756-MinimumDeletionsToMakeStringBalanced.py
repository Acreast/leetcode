# Last updated: 7/12/2025, 11:49:58 PM
class Solution:
    def minimumDeletions(self, s: str) -> int:
        a_count_right = [0] * len(s)
        for i in range(len(s) -2, -1 , -1):
            a_count_right[i] = a_count_right[i + 1]
            a_count_right[i] += 1 if s[i+1] == "a" else 0
        res = len(s)
        b_count_left = 0
        for i, c in enumerate(s):
            res = min(res, b_count_left + a_count_right[i])
            if c == "b":
                b_count_left += 1

        return res