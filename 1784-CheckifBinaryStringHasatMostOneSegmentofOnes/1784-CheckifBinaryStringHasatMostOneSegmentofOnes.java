// Last updated: 3/7/2026, 12:25:14 AM
1class Solution {
2    public boolean checkOnesSegment(String s) {
3        for (int i = 1; i < s.length(); i++) {
4            if (s.charAt(i) == '1' && s.charAt(i - 1) == '0') {
5                return false;
6            }
7        }
8        return true;
9    }
10}