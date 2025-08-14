# Last updated: 8/14/2025, 10:51:35 PM
class Solution:
    def largestGoodInteger(self, num: str) -> str:
        res = ""
        i = 0
        if num[i] == num[i + 1] == num[i + 2]:
            res = f"{num[i]}{num[i+1]}{num[i+2]}"
        for i in range(len(num) - 2):
            if num[i] == num[i + 1] == num[i + 2]:
                temp = f"{num[i]}{num[i+1]}{num[i+2]}"
                res = max(temp, res)

        return res
