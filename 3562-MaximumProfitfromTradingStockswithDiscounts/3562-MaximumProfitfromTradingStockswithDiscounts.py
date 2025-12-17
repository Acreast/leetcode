# Last updated: 12/17/2025, 10:08:46 PM
1
2class Solution:
3    def maxProfit(self, n: int, present: List[int], future: List[int], hierarchy: List[List[int]], budget: int) -> int:
4        adj_list = defaultdict(list)
5        for h in hierarchy:
6            adj_list[h[0] - 1].append(h[1] - 1)
7        
8        @lru_cache(None)
9        def dfs(employee, has_discount):
10            cost = present[employee] // 2 if has_discount else present[employee]
11            profit = future[employee] - cost
12            
13            buy_current = {cost: profit} if cost <= budget else {}
14            skip_current = {0: 0}
15            
16            for child in adj_list[employee]:
17                child_with_discount = dfs(child, True) 
18                child_no_discount = dfs(child, False) 
19                
20                new_buy = {}
21                for spent, prof in buy_current.items():
22                    for child_spent, child_prof in child_with_discount.items():
23                        total_spent = spent + child_spent
24                        if total_spent <= budget:
25                            total_prof = prof + child_prof
26                            if total_spent not in new_buy or new_buy[total_spent] < total_prof:
27                                new_buy[total_spent] = total_prof
28                buy_current = new_buy
29                
30                new_skip = {}
31                for spent, prof in skip_current.items(): 
32                    for child_spent, child_prof in child_no_discount.items():
33                        total_spent = spent + child_spent
34                        if total_spent <= budget:
35                            total_prof = prof + child_prof
36                            if total_spent not in new_skip or new_skip[total_spent] < total_prof:
37                                new_skip[total_spent] = total_prof
38                skip_current = new_skip
39            
40            result = {} 
41            for spent, prof in buy_current.items():
42                if spent not in result or result[spent] < prof:
43                    result[spent] = prof
44            for spent, prof in skip_current.items():
45                if spent not in result or result[spent] < prof:
46                    result[spent] = prof
47            
48            return result
49        
50        result = dfs(0, False)
51        return max(result.values()) if result else 0