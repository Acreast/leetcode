# Last updated: 12/26/2025, 6:08:27 PM
1class Solution:
2    def bestClosingTime(self, customers: str) -> int:
3        penalty = Counter(customers)["Y"]
4        min_penalty = [0, penalty]
5        for i,char in enumerate(customers):
6            if char == "Y":
7                penalty -= 1
8                if penalty < min_penalty[1]:
9                    min_penalty = [i, penalty]
10            else:
11                if penalty - 1 < min_penalty[1]:
12                    min_penalty = [i, penalty - 1]
13                penalty += 1
14            
15        if penalty - 1 < min_penalty[1]:
16            return len(customers)
17        return min_penalty[0]
18
19                
20                    
21
22
23