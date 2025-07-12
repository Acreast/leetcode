# Last updated: 7/12/2025, 11:48:46 PM
class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        part_len = len(part)
        part_last_char = part[-1]
        res_stack = []

        for c in s:
            res_stack.append(c)

            if c != part_last_char:
                continue
            
            if not len(res_stack) >= part_len:
                continue
            
            if "".join(res_stack[-part_len:]) == part:
                del res_stack[-part_len:]
        
        return "".join(res_stack)
                