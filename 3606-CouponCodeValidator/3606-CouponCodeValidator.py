# Last updated: 12/13/2025, 4:56:50 PM
1class Solution:
2    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
3        
4        res = []
5        businessLine_map = {
6            "electronics": 0,
7            "grocery": 1,
8            "pharmacy": 2,
9            "restaurant": 3
10        }
11        for i, c in enumerate(code):
12            if not re.match(r'^[a-zA-Z0-9_]+$', c):
13                continue
14            if not businessLine[i] in ["electronics", "grocery", "pharmacy", "restaurant"]:
15                continue
16            if not isActive[i]:
17                continue
18            res.append((c, businessLine_map[businessLine[i]]))
19        res.sort(
20            key=lambda x: (x[1], x[0])
21        )
22        sorted_res = [code for code, _ in res]
23        return sorted_res
24            
25                
26                    
27