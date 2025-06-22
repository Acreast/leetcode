# Last updated: 6/22/2025, 10:09:07 PM
class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        res = []
        sub_string = ""
        for c in s:
            sub_string += c
            if len(sub_string) == k:
                res.append(sub_string)
                sub_string = ""
        
        if len(sub_string) != 0:
            while len(sub_string) != k:
                sub_string += fill
            res.append(sub_string)
        
        return res