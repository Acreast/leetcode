# Last updated: 9/12/2026, 12:23:21 AM
1class Solution:
2    def totalNumbers(self, digits: List[int]) -> int:
3        n = len(digits)
4        seen = set()
5
6        for h in range(n):
7            if digits[h] == 0:
8                continue
9            
10            for t in range(n):
11                if t == h:
12                    continue
13                
14                for u in range(n):
15                    if u == h or u == t:
16                        continue
17                    
18                    if digits[u] % 2 != 0:
19                        continue
20                    
21                    num = digits[h] * 100 + digits[t] * 10 + digits[u]
22                    seen.add(num)
23        
24        return len(seen)