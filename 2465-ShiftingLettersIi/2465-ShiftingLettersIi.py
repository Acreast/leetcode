# Last updated: 7/12/2025, 11:46:25 PM
class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        prefix_diff = [0] * (len(s) + 1)
        for left, right, d in shifts:
            prefix_diff[right + 1] += 1 if d else -1
            prefix_diff[left] += -1 if d else 1

        res = [ord(c) - ord("a") for c in s]
        diff = 0
        for i in reversed(range(len(prefix_diff))):
            diff += prefix_diff[i]

            res[i - 1] = (diff + res[i - 1]) % 26

        s = [chr(ord("a") + c) for c in res]
        return "".join(s)

