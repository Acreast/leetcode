// Last updated: 6/22/2026, 12:54:12 AM
1class Solution {
2    public int maxIceCream(int[] costs, int coins) {
3        int max = 0;
4        for (int c: costs)
5            if (c > max) 
6                max = c;
7        int[] freq = new int[max + 1];
8        for (int c: costs) {
9            freq[c] += 1;
10        }
11
12        int res = 0;
13        for (int i = 0; i < max + 1; i ++) {
14            if (freq[i] == 0)
15                continue;
16            
17            if (coins < i)
18                break;
19            
20            int count_to_buy = Math.min(freq[i], coins/i);
21            res += count_to_buy;
22            coins -= count_to_buy * i;
23
24        }
25
26        return res;
27    }
28}