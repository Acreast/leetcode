// Last updated: 2/19/2026, 11:22:12 PM
1class Solution {
2    public int countBinarySubstrings(String s) {
3        List<Integer> groups = new ArrayList<>();
4        char prev = s.charAt(0);
5        int counter = 1;
6        for (int i = 1; i < s.length(); i++) {
7            char cur_char = s.charAt(i);
8            if (cur_char != prev) {
9                groups.add(counter);
10                counter = 1;
11                prev = cur_char;
12            } else {
13                counter += 1;
14            }
15        }
16        groups.add(counter);
17
18        int prev_group = groups.get(0);
19        int res = 0;
20        for (int i = 1; i < groups.size(); i++ ) {
21            int cur_group = groups.get(i);
22            res += Math.min(prev_group,cur_group);
23            prev_group = cur_group;
24        }
25        return res;
26    }
27}