// Last updated: 6/1/2026, 8:57:43 PM
1class Solution {
2    public int minimumCost(int[] cost) {
3        int res = 0;
4        Arrays.sort(cost);
5        
6        
7        int count = 0;
8        
9        
10        for (int i = cost.length - 1; i >= 0; i--) {
11            count++;
12            if (count == 3) {
13                
14                count = 0;
15                continue;
16            }
17            res += cost[i];
18        }
19        return res;
20    }
21}