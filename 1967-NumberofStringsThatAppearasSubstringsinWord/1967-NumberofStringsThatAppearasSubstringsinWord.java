// Last updated: 6/29/2026, 11:12:34 PM
1class Solution {
2    public int numOfStrings(String[] patterns, String word) {
3        int res = 0;
4        for (String pattern : patterns) {
5            if (word.contains(pattern))
6                res ++;
7        }
8        return res;
9    }
10}