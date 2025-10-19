# Last updated: 10/19/2025, 8:14:59 PM
class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        n = len(s)

        increment_map = {str(n):str((n+a) % 10) for n in range (10)}

        def add_operation(s):
            res = ""
            for i in range(n):
                res += s[i] if i % 2 == 0 else increment_map[s[i]]
            return res

        def rotation_operation(s):
            return s[n - b:] + s[:n - b]
        
        seen = set()
        def dfs(s):
            if s in seen:
                return
            seen.add(s)
            dfs(add_operation(s))
            dfs(rotation_operation(s))
            return
        dfs(s)
        return min(seen)