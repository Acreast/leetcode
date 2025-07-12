# Last updated: 7/12/2025, 11:44:44 PM
class Solution:
    def countSeniors(self, details: List[str]) -> int:
        res = 0
        for detail in details:
            age = int(detail[-4]) * 10 + int(detail[-3]) 
            if age > 60:
                res += 1

        return res
