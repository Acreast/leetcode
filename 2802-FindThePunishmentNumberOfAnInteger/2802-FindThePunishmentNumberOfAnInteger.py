# Last updated: 7/12/2025, 11:44:33 PM
class Solution:
    def punishmentNumber(self, n: int) -> int:
        res = 0

        def partition(i, cur, target, string):
            if i == len(string) and cur == target:
                return True
            
            for j in range(i, len(string)):
                if partition(j + 1, cur + int(string[i:j+1]), target, string):
                    return True
            
            return False

        for i in range(1, n + 1):
            if partition(0, 0, i, str(i*i)):
                res += i * i

        return res