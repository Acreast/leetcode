# Last updated: 5/11/2025, 10:56:08 PM
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        l = 0
        window, target = {}, {}
        res = [-1, -1]
        res_len = float("infinity")

        if t == "":
            return ""

        for c in t:
            target[c] = 1 + target.get(c, 0)
        have = 0
        need = len(target)
        
        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)
            if c in target and window[c] == target[c]:
                have += 1
            
            while have == need:
                if (r - l + 1) < res_len:
                    res = [l, r]
                    res_len = (r - l + 1)
                window[s[l]] -= 1
                if s[l] in target and window[s[l]] < target[s[l]]:
                    have -= 1
                l += 1
        
        l, r = res
        return s[l:r + 1] if res_len != float("infinity") else ""
           
            



        