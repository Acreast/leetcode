// Last updated: 4/20/2026, 11:24:00 PM
1class Solution {
2    public int maxDistance(int[] colors) {
3        ArrayList<Integer> seen = new ArrayList<Integer>();
4        int res = -Integer.MAX_VALUE;
5        for(int i = 0; i < colors.length - 1; i ++) {
6            int cur_color = colors[i];
7            if (seen.contains(cur_color)) {
8                continue;
9            }
10            seen.add(cur_color);
11            for (int j = i + 1; j < colors.length; j ++) {
12                int next_color = colors[j];
13                if (cur_color != next_color) {
14                    res = Math.max(res, j - i);
15                }
16            }
17            
18        }
19
20        return res;
21
22
23    }
24}