# Last updated: 8/16/2025, 10:30:32 AM
class Solution:
    def maximum69Number (self, num: int) -> int:
        
        num_str = str(num)
        res_str = ""
        for i in range(len(num_str)):
            if num_str[i] == "6":
                res_str += "9"
                if i != len(num_str) - 1:
                    res_str += num_str[i + 1:]
                break
            else:
                res_str += num_str[i]
        
        return int(res_str)
        
