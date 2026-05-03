// Last updated: 5/3/2026, 11:12:53 PM
1class Solution {
2    public boolean rotateString(String s, String goal) {
3        
4        int n = s.length();
5        if (n != goal.length()) {
6            return false;
7        }
8
9        String concat_s = s.concat(s);
10        return concat_s.contains(goal);
11    }
12}