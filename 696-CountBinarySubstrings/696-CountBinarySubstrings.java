// Last updated: 2/19/2026, 11:31:06 PM
1class Solution {
2    public int countBinarySubstrings(String s) {
3        int res = 0;
4        int prevGroup = 0;
5        int curGroup = 1;
6        for (int i = 1; i < s.length();i ++) {
7            if (s.charAt(i) == s.charAt(i - 1)) {
8                curGroup += 1;
9            } else {
10                res += Math.min(prevGroup, curGroup);
11                prevGroup = curGroup;
12                curGroup = 1;
13            }
14        }
15
16        return res + Math.min(curGroup,prevGroup);
17    }
18}